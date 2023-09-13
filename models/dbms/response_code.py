
import sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from database.conn import Base

from models.dbms.base_mixin import BaseMixin


class ResponseCode(Base, BaseMixin):
    __tablename__ = "response_code"
    __table_args__ = {"schema": "public"}
    code = Column(String)
    comment = Column(String)

    def __str__(self):
        return '{0},{1},{2},{3} '.format(self.id, self.uuid, self.code, self.comment)
