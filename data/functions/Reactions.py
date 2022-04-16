from telegram.user import User as TelegramUser
from data.db.db_functions import get_news_info, edit_user_interests


def update_interests(user: TelegramUser, reaction: str) -> None:
    mark, news_id = reaction.split()
    news_id = int(news_id)
    news = get_news_info(news_id)
    main_interests_indexes = []
    for index in range(len(news[1:])):
        if news[index] == max(news[1:]):
            main_interests_indexes.append(index)
    edit_user_interests(user, mark, main_interests_indexes)
