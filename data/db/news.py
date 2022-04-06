import sqlalchemy
from datetime import datetime
from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # check Image
    date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
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
    def __init__(self, text: str, date: datetime,
                 rus_plt: int, usa_plt: int, eur_plt: int, ftb_spt: int,
                 bsk_spt: int, hck_spt: int, spc_sci: int, mth_sci: int,
                 hst_sci: int):
        self.text = text
        self.date = date
        self.rus_plt = rus_plt
        self.usa_plt = usa_plt
        self.eur_plt = eur_plt
        self.ftb_spt = ftb_spt
        self.bsk_spt = bsk_spt
        self.spc_sci = spc_sci
        self.hck_spt = hck_spt
        self.mth_sci = mth_sci
        self.hst_sci = hst_sci
