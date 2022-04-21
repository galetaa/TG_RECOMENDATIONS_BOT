# -----------------------------------------------------------------------------
# Файл реализующий выборки для пользователя наиболее подходящей новости.
# -----------------------------------------------------------------------------
from telegram.user import User as TelegramUser
from data.db.db_functions import get_user_interests, get_news
from data.db.db_functions import get_news_text, edit_user_read_news


# ф-ия получает все новости и выбирает непрочитанные и наиболее подходящие
def choose_news_for_user(user: TelegramUser) -> int:
    interests = get_user_interests(user)
    read_news = list(map(int, interests[1].split()))

    news = list(filter(lambda x: x[0] not in read_news, get_news()))

    # в цикле происходит перемножение оценок новости по категориям с оценками
    # пользователя по таким же категориям, в результате выбираются наиболее
    # подходящая новость по колличеству итоговых "очков"
    for new_s in news:
        for i in range(1, len(new_s) - 1):
            new_s[i] *= interests[2:][i]

    if len(news) == 0:
        return -1

    result = sorted(news, key=lambda x: sum(x[1:]))[-1]
    return result[0]


# ф-ия получает новость и назначает её для пользователя
def assign_news_to_user(user: TelegramUser) -> list:
    news_id = choose_news_for_user(user)
    if news_id == -1:
        return [-1, -1]
    news_id_and_text = get_news_text(news_id)
    edit_user_read_news(user=user, new_news=str(news_id) + ' ')
    return news_id_and_text
