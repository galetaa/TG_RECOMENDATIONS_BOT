# -----------------------------------------------------------------------------
# Файл реализующий распределение новостей по категориям.
# -----------------------------------------------------------------------------
from data.containers.key_words import categories
from telethon.sync import Message
from data.db import db_session
from data.db.news import News
from data.functions import TextFormatter
from datetime import datetime


# ф-ия создающая оценки новостям по разным категориям
def get_categories_marks(text: str, minimum_mark: int = 0) -> list:
    marks = [0] * len(categories)
    words_list = TextFormatter.formate_text(text)

    # цикл проходит по отформатированному тексту новости и каждое словао
    # проверяет на соответствие категории
    for word in words_list:

        for i in range(len(categories)):
            if word in categories[i]:
                marks[i] += 1

    if minimum_mark != 0:

        for i in range(len(marks)):
            if marks[i] < minimum_mark:
                marks[i] = 0
    return marks


# ф-ия добавляющая новость в бд
def add_news(msg: Message, minimum_mark: int = 0) -> None:
    message_text = msg.message
    if message_text == '' or message_text is None:
        return None

    message_categories_marks = get_categories_marks(message_text, minimum_mark)
    param_list = [message_text] + message_categories_marks

    db_session.global_init()
    db_sess = db_session.create_session()

    news = News(*param_list)
    db_sess.add(news)
    db_sess.commit()
    db_sess.close()
