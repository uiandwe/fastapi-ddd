from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from database.conn import Base


class Allocations(Base):
    __tablename__ = "allocations"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    orderline_id = Column(Integer, ForeignKey("order_lines.id"))
    batch_id = Column(Integer, ForeignKey("batches.id"))

