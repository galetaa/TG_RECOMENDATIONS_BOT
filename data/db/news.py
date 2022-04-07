from sqlalchemy import Column, Integer, String
from .db_session import SqlAlchemyBase


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
    mth_sci = Column(Integer, nullable=True, default=0)
    hst_sci = Column(Integer, nullable=True, default=0)

    # tbc...
    def __init__(self, text: str,
                 rus_plt: int, usa_plt: int, eur_plt: int, ftb_spt: int,
                 bsk_spt: int, hck_spt: int, spc_sci: int, mth_sci: int,
                 hst_sci: int):
        self.text = text
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
        return [self.id, self.rus_plt, self.usa_plt,
                self.eur_plt, self.ftb_spt, self.bsk_spt, self.hck_spt,
                self.spc_sci, self.mth_sci, self.hst_sci]
