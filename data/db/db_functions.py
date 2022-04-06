from . import db_session
from data.containers.config import db_path
from data.db.users import User
from telegram.user import User as TelegramUser


def user_exists(user_to_check: TelegramUser) -> bool:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    user_id = user_to_check.id
    return db_sess.query(User.id).filter_by(id=user_id).first() is not None


def register_user(user_to_register: TelegramUser) -> None:
    db_session.global_init(db_path)
    db_sess = db_session.create_session()
    user = User()
    user.id = user_to_register.id
    if user_to_register.first_name is not None:
        user.first_name = user_to_register.first_name
    if user_to_register.last_name is not None:
        user.last_name = user_to_register.first_name
    db_sess.add(user)
    db_sess.commit()
