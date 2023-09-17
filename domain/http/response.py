
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import Optional, List


class SavedQuestions(BaseModel):
    """
    """
    id: int
    possed_qst: str
    question: str
    response_code: Optional[str] = None
    uuid: UUID
    hit_count: int
    create_at: datetime
    modified_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None
    is_use: bool


class ReplyCode(BaseModel):
    """
    """
    code: str
    comment: str
    uuid: UUID
    create_at: datetime
    modified_at: Optional[datetime] = None

