from sqlalchemy import Column, String, Integer
from database.conn import Base


class OrderLines(Base):
    __tablename__ = "order_lines"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String)
    qty = Column(Integer)
    orderid = Column(String)