from telegram.user import User as TelegramUser
from data.db.db_functions import get_user_interests, get_news
from data.db.db_functions import get_news_text, edit_user_read_news


def choose_news_for_user(user: TelegramUser) -> int:
    interests = get_user_interests(user)
    read_news = list(map(int, interests[1].split()))
    news = list(filter(lambda x: x[0] not in read_news, get_news()))
    for new_s in news:
        for i in range(1, len(new_s) - 1):
            new_s[i] *= interests[2:][i]
    result = sorted(news, key=lambda x: sum(x[1:]))[-1]
    if result:
        return result[0]
    else:
        return -1


def assign_news_to_user(user: TelegramUser) -> list:
    news_id = choose_news_for_user(user)
    if news_id == -1:
        return [-1, -1]
    news_id_and_text = get_news_text(news_id)
    edit_user_read_news(user=user, new_news=str(news_id) + ' ')
    return news_id_and_text
