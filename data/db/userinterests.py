from sqlalchemy import Column, Integer, String
from data.db.db_session import SqlAlchemyBase


class UserInterests(SqlAlchemyBase):
    __tablename__ = 'users_interests'

    user_id = Column(Integer, primary_key=True)
    read_news = Column(String, nullable=True, default='')

    rus_plt = Column(Integer, nullable=True, default=0)
    usa_plt = Column(Integer, nullable=True, default=0)
    eur_plt = Column(Integer, nullable=True, default=0)

    ftb_spt = Column(Integer, nullable=True, default=0)
    bsk_spt = Column(Integer, nullable=True, default=0)
    hck_spt = Column(Integer, nullable=True, default=0)

    spc_sci = Column(Integer, nullable=True, default=0)
    all_sci = Column(Integer, nullable=True, default=0)
    hst_sci = Column(Integer, nullable=True, default=0)

    cin_ent = Column(Integer, nullable=True, default=0)
    msc_ent = Column(Integer, nullable=True, default=0)
    sks_tch = Column(Integer, nullable=True, default=0)
    itc_tch = Column(Integer, nullable=True, default=0)
    gms_tch = Column(Integer, nullable=True, default=0)
    bsn_tch = Column(Integer, nullable=True, default=0)

    # tbc...
    def __init__(self, user_id: int = 0, read_news: str = '',
                 rus_plt: int = 0, usa_plt: int = 0, eur_plt: int = 0,
                 ftb_spt: int = 0, bsk_spt: int = 0, hck_spt: int = 0,
                 spc_sci: int = 0, all_sci: int = 0, hst_sci: int = 0,
                 cin_ent: int = 0, msc_ent: int = 0, sks_tch: int = 0,
                 itc_tch: int = 0, gms_tch: int = 0, bsn_tch: int = 0):
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
        self.all_sci = all_sci
        self.hst_sci = hst_sci
        self.cin_ent = cin_ent
        self.msc_ent = msc_ent
        self.sks_tch = sks_tch
        self.itc_tch = itc_tch
        self.gms_tch = gms_tch
        self.bsn_tch = bsn_tch

    def __list__(self):
        return [self.user_id, self.read_news,
                self.rus_plt, self.usa_plt, self.eur_plt, self.ftb_spt,
                self.bsk_spt, self.hck_spt, self.spc_sci, self.all_sci,
                self.hst_sci, self.cin_ent, self.msc_ent, self.sks_tch,
                self.itc_tch, self.gms_tch, self.bsn_tch]
