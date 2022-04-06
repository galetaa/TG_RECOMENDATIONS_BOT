import sqlalchemy
from .db_session import SqlAlchemyBase
from .users import User


class User(SqlAlchemyBase):
    __tablename__ = 'users_interests'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(
        User.id), primary_key=True)
    read_news = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    rus_plt = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    usa_plt = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    eur_plt = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    ftb_spt = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    bsk_spt = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    hck_spt = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    spc_sci = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    mth_sci = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    hst_sci = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)



    # tbc...
