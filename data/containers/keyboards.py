from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton

settings_keyboard = ReplyKeyboardMarkup([['Сообщения по-расписанию'],
                                         ['Удалить мои данные'],
                                         ['Назад']],
                                        one_time_keyboard=True)

get_news_keyboard = ReplyKeyboardMarkup([['Получить новость']],
                                        one_time_keyboard=True)

reactions_keyborad = InlineKeyboardMarkup.from_row(
    [InlineKeyboardButton(text='👍', callback_data='+'),
     InlineKeyboardButton(text='👎', callback_data='-')])
