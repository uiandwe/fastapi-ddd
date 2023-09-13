from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from database.conn import Base


class Notice(Base):
    __tablename__ = "notice"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    chnl_id = Column(String)
    body_cntt = Column(String)
    regpe_id = Column(String)
    reg_dts = Column(DateTime(timezone=True))
    modpe_id = Column(String)
    mod_dts = Column(DateTime(timezone=True))
    notice_desc = Column(String)

    def __str__(self):
        return '{0},{1},{2},{3}'.format(self.id, self.body_cntt, self.regpe_id, self.modpe_id)
