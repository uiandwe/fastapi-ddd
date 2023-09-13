
from pydantic import BaseModel
from typing import Optional


class CntRptModel(BaseModel):
    """
    id :
    cnt :
    ex)
        seq:2878162
        cnt:23
    """
    id: int
    cnt: Optional[int] = None
    used_at: str = ''


class ResModel(BaseModel):
    code: int
    message: Optional[str] = None
    result: CntRptModel


class Question(BaseModel):
    decomposed_quest: str
    question: str
    correlation_id: str