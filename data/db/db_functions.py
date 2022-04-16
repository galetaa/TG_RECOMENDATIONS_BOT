from data.db import db_session
from data.containers.config import db_path
from data.db.users import User
from data.db.news import News
from data.db.userinterests import UserInterests
from telegram.user import User as TelegramUser


def user_exists(user_to_check: TelegramUser) -> bool:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    user_id = user_to_check.id
    db_sess.close()
    return db_sess.query(User.id).filter_by(id=user_id).first() is not None


def get_news(id_only: bool = False) -> list:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    if id_only:
        news_db = [x[0] for x in db_sess.query(News.id).distinct().all()]
    else:
        news_db = [x.__list__() for x in db_sess.query(News).distinct().all()]
    db_sess.close()
    return news_db


def get_news_text(news_id: int) -> list:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    news_db = db_sess.query(News).filter_by(id=news_id).first()
    db_sess.close()
    return [news_db.id, news_db.text]


def get_news_info(news_id: int) -> list:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    news_db = db_sess.query(News).filter_by(id=news_id).first()
    db_sess.close()
    return news_db.__list__()


def get_user_interests(user: TelegramUser) -> list:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    user_db = db_sess.query(UserInterests).filter_by(
        user_id=user.id).one().__list__()
    db_sess.close()
    return user_db


def edit_user_read_news(user: TelegramUser, new_news: str = '',
                        clear: bool = False) -> None:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    user_db = db_sess.query(UserInterests).filter_by(user_id=user.id).first()
    if clear:
        user_db.read_news = ''
    else:
        pre_str = user_db.read_news
        user_db.read_news = pre_str + new_news
    db_sess.commit()
    db_sess.close()


def edit_user_interests(user: TelegramUser, mark: str,
                        interests: list) -> None:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    user_db = db_sess.query(UserInterests).filter_by(user_id=user.id).first()
    params = user_db.__list__()
    db_sess.delete(user_db)
    if mark == '+':
        for interest_index in interests:
            params[interest_index + 1] += 1
    elif mark == '-':
        for interest_index in interests:
            params[interest_index + 1] -= 1
    user_db = UserInterests(*params)
    db_sess.add(user_db)
    db_sess.commit()
    db_sess.close()


def delete_news(news_id: int) -> None:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    news_db = db_sess.query(News).filter_by(id=news_id).first()
    db_sess.delete(news_db)
    db_sess.commit()
    db_sess.close()


def register_user(user_to_register: TelegramUser) -> None:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()

    user = User()
    user.id = user_to_register.id
    user_interests = UserInterests()
    user_interests.user_id = user_to_register.id

    if user_to_register.first_name is not None:
        user.first_name = user_to_register.first_name
    if user_to_register.last_name is not None:
        user.last_name = user_to_register.first_name

    db_sess.add(user)
    db_sess.add(user_interests)
    db_sess.commit()
    db_sess.close()
