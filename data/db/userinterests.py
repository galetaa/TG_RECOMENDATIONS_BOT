from sqlalchemy import Column, Integer, String, ForeignKey
from data.db.db_session import SqlAlchemyBase
from data.db.users import User


class UserInterests(SqlAlchemyBase):
    __tablename__ = 'users_interests'

    user_id = Column(Integer, ForeignKey(
        User.id), primary_key=True)
    read_news = Column(String, nullable=True, default='')

    rus_plt = Column(Integer, nullable=True, default=0)
    usa_plt = Column(Integer, nullable=True, default=0)
    eur_plt = Column(Integer, nullable=True, default=0)

    ftb_spt = Column(Integer, nullable=True, default=0)
    bsk_spt = Column(Integer, nullable=True, default=0)
    hck_spt = Column(Integer, nullable=True, default=0)

    spc_sci = Column(Integer, nullable=True, default=0)
    mth_sci = Column(Integer, nullable=True, default=0)
    hst_sci = Column(Integer, nullable=True, default=0)

    # tbc...
    def __init__(self, user_id: int = 0, read_news: str = '',
                 rus_plt: int = 0, usa_plt: int = 0, eur_plt: int = 0,
                 ftb_spt: int = 0, bsk_spt: int = 0, hck_spt: int = 0,
                 spc_sci: int = 0, mth_sci: int = 0, hst_sci: int = 0):
        if user_id != 0:
            self.user_id = user_id
        self.read_news = read_news
        self.rus_plt = rus_plt
        self.usa_plt = usa_plt
        self.eur_plt = eur_plt
        self.ftb_spt = ftb_spt
        self.bsk_spt = bsk_spt
        self.spc_sci = spc_sci
        self.hck_spt = hck_spt
        self.mth_sci = mth_sci
        self.hst_sci = hst_sci

    def __list__(self):
        return [self.user_id, self.read_news, self.rus_plt, self.usa_plt,
                self.eur_plt, self.ftb_spt, self.bsk_spt, self.hck_spt,
                self.spc_sci, self.mth_sci, self.hst_sci]
