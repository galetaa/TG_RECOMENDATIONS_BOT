import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import JobQueue, CallbackQueryHandler
from data.containers import pattern_messages
from data.containers.config import bot_token
from data.containers import keyboards
from data.functions import Chooser, Spider, Reactions
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
    news_id, text = Chooser.assign_news_to_user(user)
    keyboard = keyboards.get_reactions_keyboard(news_id)
    update.message.reply_text(text,
                              reply_markup=keyboard)


def reactions(update, context):
    user = update.callback_query.from_user
    query = update.callback_query
    variant = query.data
    query.answer()
    Reactions.update_interests(user, variant)


def adding_handlers(disp):
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("settings", settings))
    disp.add_handler(MessageHandler(Filters.text('Получить новость'),
                                    news))
    disp.add_handler(CallbackQueryHandler(reactions))
    # disp


def run_spider(job_que):
    Spider.parse_all_channels()
    job_que.run_repeating(run_spider(job_que), interval=datetime.timedelta(
        hours=1))


def main():
    Spider.parse_all_channels()
    TOKEN = bot_token
    UPDATER = Updater(TOKEN, use_context=True)
    DISPATCHER = UPDATER.dispatcher

    job = UPDATER.job_queue
    job.run_repeating(run_spider(job), interval=datetime.timedelta(hours=1))
    adding_handlers(DISPATCHER)

    UPDATER.start_polling()
    UPDATER.idle()


if __name__ == '__main__':
    main()
