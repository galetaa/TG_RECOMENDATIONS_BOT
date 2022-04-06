from telegram import ReplyKeyboardMarkup

settings_keyboard = ReplyKeyboardMarkup([['Сообщения по-расписанию'],
                                         ['Удалить мои данные'],
                                         ['Назад']],
                                        one_time_keyboard=True)

get_news_keyboard = ReplyKeyboardMarkup(['Получить новость'],
                                        one_time_keyboard=True)
