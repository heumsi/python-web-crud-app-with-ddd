from pydantic import BaseModel


class TokenPayload(BaseModel):
    user_id: str


class User(BaseModel):
    id: str
    password: str
