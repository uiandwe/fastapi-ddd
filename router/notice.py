# pylint: disable=E0611,E0401
import json
import sys
import os

from fastapi import APIRouter, Depends, HTTPException, Path, Request
from datetime import datetime
from typing import Optional

from models.dbms.notice import Notice


from models.http.request import NoticeRequest

from database.aws_conn import aws_db

from sqlalchemy.orm import Session

from utils.consist import api_desc
from sqlalchemy import func

router = APIRouter(prefix="/notice")


class Dummy(object):
    def __init__(self, body_cntt, brch_id):
        self.body_cntt = body_cntt
        self.brch_id = brch_id


def replace_text(t):
    return t.replace("'", "\"").replace("\n", "")

