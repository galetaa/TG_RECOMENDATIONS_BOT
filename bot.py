from telegram.ext import Updater, CommandHandler
from data.containers import pattern_messages
from data.containers.config import bot_token
from data.containers import keyboards
import data.db.db_functions as db_functions


def start(update, context):
    user = update.message.from_user
    if db_functions.user_exists(user):
        update.message.reply_text(pattern_messages.YOU_HAVE_REGISTERED_MESSAGE)
    else:
        db_functions.register_user(user)
        update.message.reply_text(pattern_messages.START_MESSAGE)


def settings(update, context):
    update.message.reply_text(pattern_messages.SETTINGS_MESSAGE,
                              reply_markup=keyboards.settings_keyboard)


def adding_handlers(disp):
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("settings", settings))


def main():
    TOKEN = bot_token
    UPDATER = Updater(TOKEN, use_context=True)
    DISPATCHER = UPDATER.dispatcher
    adding_handlers(DISPATCHER)

    UPDATER.start_polling()
    UPDATER.idle()


if __name__ == '__main__':
    main()
