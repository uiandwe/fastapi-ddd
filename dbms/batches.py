from email.policy import default
import sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.conn import Base


class Batches(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reference = Column(String)
    sku = Column(String)
    _purchased_quantity = Column(Integer)
    eta = Column(DateTime)
