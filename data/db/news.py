from sqlalchemy import Column, Integer, String
from data.db.db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=True)
    image = Column(String, nullable=True)  # check Image

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
    def __init__(self, text: str,
                 rus_plt, usa_plt, eur_plt, ftb_spt, bsk_spt, hck_spt, spc_sci,
                 all_sci, hst_sci, cin_ent, msc_ent, sks_tch, itc_tch, gms_tch,
                 bsn_tch):
        self.text = text
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
        return [self.id,
                self.rus_plt, self.usa_plt, self.eur_plt, self.ftb_spt,
                self.bsk_spt, self.hck_spt, self.spc_sci, self.all_sci,
                self.hst_sci, self.cin_ent, self.msc_ent, self.sks_tch,
                self.itc_tch, self.gms_tch, self.bsn_tch]
