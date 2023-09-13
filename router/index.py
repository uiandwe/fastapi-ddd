# pylint: disable=E0611,E0401

from fastapi import APIRouter
from utils.consist import api_desc
from os import environ

router = APIRouter()

@router.get("/", description=api_desc['index'], summary='healthcheck')
async def index():
    return {"detail": 200,
            "env": environ.get("API_ENV", "local")}
