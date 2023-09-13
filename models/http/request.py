from pydantic import BaseModel, validator, root_validator
from typing import Optional, List
from typing import Union
from datetime import date, datetime


class NoticeRequest(BaseModel):
    """
    """
    brch_id: str = 'all'
    chnl_id: str = 'A'
    body_cntt: str = ''
    notice_desc: str = ''
    gubun: str = ''



class NotAssignTimeRequestCreate(BaseModel):
    type: str = "DAY_CYCLE"
    hour_from: int
    hour_to: int
    days: Optional[List[int]] = None
    message: str
    date: Optional[str] = None
    modpe_id: Optional[str] = None
    mod_dts: Optional[str] = None

    @root_validator()
    def check_column_values(cls, values):
        if values.get('days') is None and values.get('date') is None:
            raise ValueError("days와 date 두 개의 데이터중 하나라도 Null이 아니어야 합니다.")
        return values


class NotAssignTimeRequestDelete(BaseModel):
    hour_from: int
    hour_to: int
    days: List[int]
