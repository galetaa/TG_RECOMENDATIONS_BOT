# -----------------------------------------------------------------------------
# Основной файл бота. Он и запускается на хостинге.
# -----------------------------------------------------------------------------
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackQueryHandler
from data.containers import pattern_messages
from data.containers.config import bot_token
from data.containers import keyboards
from data.functions import Chooser, Spider, Reactions, Weather
import data.db.db_functions as db_functions


# ф-ия выполняющая команду "/start"
def start(update, context):
    user = update.message.from_user
    if db_functions.user_exists(user):
        update.message.reply_text(pattern_messages.YOU_HAVE_REGISTERED_MESSAGE,
                                  reply_markup=keyboards.get_news_keyboard)
    else:
        db_functions.register_user(user)
        update.message.reply_text(pattern_messages.START_MESSAGE,
                                  reply_markup=keyboards.get_news_keyboard)


# ф-ия выполняющая команду "/settings".
def settings(update, context):
    update.message.reply_text(pattern_messages.SETTINGS_MESSAGE,
                              reply_markup=keyboards.settings_keyboard)


# ф-ия для отправки новости (сообщение "Получить новость").
def news(update, context):
    user = update.message.from_user
    news_id, text = Chooser.assign_news_to_user(user)
    if news_id == -1 and text == -1:
        update.message.reply_text(pattern_messages.THERE_IS_NO_NEWS)

    else:
        # вместе с сообщением отправляет панель с реакциями
        keyboard = keyboards.get_reactions_keyboard(news_id)
        update.message.reply_text(text,
                                  reply_markup=keyboard)


# ф-ия для работы с реакциями на новости.
def reactions(update, context):
    user = update.callback_query.from_user
    query = update.callback_query
    variant = query.data
    query.answer()
    Reactions.update_interests(user, variant)


# ф-ия отвечающая на команду '/weather'
def location(update, context):
    keyboard = keyboards.get_location_keyboard
    update.message.reply_text(pattern_messages.GET_YOUR_WEATHER,
                              reply_markup=keyboard)


# ф-ия отвечающая на местоположение пользователя
def weather(update, context):
    keyboard = keyboards.get_news_keyboard
    wethr = Weather.get_weather(update.message)
    update.message.reply_text(wethr,
                              reply_markup=keyboard)


# ф-ия возвращающая пользователя к стандартному сценарию, когда он получает
# новость.
def back(update, context):
    keyboard = keyboards.get_news_keyboard
    update.message.reply_text(pattern_messages.GET_YOUR_NEWS,
                              reply_markup=keyboard)


# ф-ия добавляющая все обработчики сообщений.
def adding_handlers(disp):
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("settings", settings))
    disp.add_handler(CommandHandler("weather", location))
    disp.add_handler(MessageHandler(Filters.text(
        pattern_messages.GET_NEWS_TRIGGER), news))
    disp.add_handler(MessageHandler(Filters.text(
        pattern_messages.GET_BACK_TRIGGER), back))
    disp.add_handler(MessageHandler(Filters.location, weather))
    disp.add_handler(CallbackQueryHandler(reactions))


# основная ф-ия.
def main():
    TOKEN = bot_token
    UPDATER = Updater(TOKEN, use_context=True)
    DISPATCHER = UPDATER.dispatcher
    JOB_QUEUE = UPDATER.job_queue

    # после запуска первый раз парсит новости, затем каждый час
    # Spider.parse_all_channels()
    JOB_QUEUE.run_repeating(Spider.parse_all_channels,
                            interval=datetime.timedelta(hours=1))
    adding_handlers(DISPATCHER)
    UPDATER.start_polling()
    UPDATER.idle()


if __name__ == '__main__':
    main()
