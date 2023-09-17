from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    name: str
    id: int
    username: str
    type: str


class signup(BaseModel):
    username: str
    password: str
    name: str


class signin(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: str = None
