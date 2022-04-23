from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram import InlineKeyboardButton, KeyboardButton

settings_keyboard = ReplyKeyboardMarkup([['Удалить мои данные'],
                                         ['Назад']],
                                        one_time_keyboard=True)

get_news_keyboard = ReplyKeyboardMarkup([['Получить новость']],
                                        one_time_keyboard=False)

get_location_keyboard = ReplyKeyboardMarkup.from_button(
    KeyboardButton(text='Отправить местоположение', request_location=True),
    row_width=1, resize_keyboard=True)


def get_reactions_keyboard(news_id: int) -> InlineKeyboardMarkup:
    reactions_keyboard = InlineKeyboardMarkup.from_row(
        [InlineKeyboardButton(text='👍',
                              callback_data='+' + ' ' + str(news_id)),
         InlineKeyboardButton(text='👎',
                              callback_data='-' + ' ' + str(news_id), )], )
    return reactions_keyboard
