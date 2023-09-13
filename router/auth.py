from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import status, HTTPException
import requests, json

from models.dbms.agent_user import AgentUser
from models.http.auth import Token, signup, signin
from passlib.context import CryptContext
from jose import JWTError, jwt
from utils.consist import api_desc

from common.config import conf


router = APIRouter(prefix="/auth")

