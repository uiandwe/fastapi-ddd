from fastapi import APIRouter, Depends, Request, HTTPException
from services.allocate import allocate, InvalidSku
from domain.exceptions import OutOfStock
from domain.data_class import OrderLine
from repository.sql_repository import SqlAlchemyRepository
from database.conn import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel

router = APIRouter(prefix="/allocate")


class Item(BaseModel):
    orderid: str
    sku: str
    qty: int

@router.post("")
def allocate_endpoint(item: Item):
                      #session: Session = Depends(SessionLocal)):

    repo = SqlAlchemyRepository(SessionLocal())
    line = OrderLine(
        item.orderid, item.sku, item.qty,
    )
    try:
        batchref = allocate(line, repo, SessionLocal())
    except (OutOfStock, InvalidSku) as e:
        raise HTTPException(status_code=400, detail={"message": str(e)})

    return {"batchref": batchref}
