from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from data.containers import pattern_messages
from data.containers.config import bot_token
from data.containers import keyboards
from data.functions import Chooser, Spider
import data.db.db_functions as db_functions


def start(update, context):
    user = update.message.from_user
    if db_functions.user_exists(user):
        update.message.reply_text(pattern_messages.YOU_HAVE_REGISTERED_MESSAGE,
                                  reply_markup=keyboards.get_news_keyboard)
    else:
        db_functions.register_user(user)
        update.message.reply_text(pattern_messages.START_MESSAGE,
                                  reply_markup=keyboards.get_news_keyboard)


def settings(update, context):
    update.message.reply_text(pattern_messages.SETTINGS_MESSAGE,
                              reply_markup=keyboards.settings_keyboard)


def news(update, context):
    user = update.message.from_user
    text = Chooser.assign_news_to_user(user)[1]
    update.message.reply_text(text,
                              reply_markup=keyboards.get_news_keyboard)


def adding_handlers(disp):
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("settings", settings))
    disp.add_handler(MessageHandler(Filters.text('Получить новость'),
                                    news))


def main():
    Spider.parse_all_channels()
    TOKEN = bot_token
    UPDATER = Updater(TOKEN, use_context=True)
    DISPATCHER = UPDATER.dispatcher
    adding_handlers(DISPATCHER)

    UPDATER.start_polling()
    UPDATER.idle()


if __name__ == '__main__':
    main()
