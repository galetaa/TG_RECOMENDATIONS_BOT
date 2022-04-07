from sqlalchemy import Column, Integer, String, ForeignKey
from .db_session import SqlAlchemyBase
from .users import User


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

    def __list__(self):
        return [self.user_id, self.read_news, self.rus_plt, self.usa_plt,
                self.eur_plt, self.ftb_spt, self.bsk_spt, self.hck_spt,
                self.spc_sci, self.mth_sci, self.hst_sci]
