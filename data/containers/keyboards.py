from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton

settings_keyboard = ReplyKeyboardMarkup([['Сообщения по-расписанию'],
                                         ['Удалить мои данные'],
                                         ['Назад']],
                                        one_time_keyboard=True)

get_news_keyboard = ReplyKeyboardMarkup([['Получить новость']],
                                        one_time_keyboard=False)


def get_reactions_keyboard(news_id: int) -> InlineKeyboardMarkup:
    reactions_keyborad = InlineKeyboardMarkup.from_row(
        [InlineKeyboardButton(text='👍',
                              callback_data='+' + ' ' + str(news_id)),
         InlineKeyboardButton(text='👎',
                              callback_data='-' + ' ' + str(news_id), )], )
    return reactions_keyborad
