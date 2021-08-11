from pydantic import BaseModel

from app.users.domain.model import User
from app.users.domain.repository import UserRepository


class CreateUserRequest(BaseModel):
    id: str
    name: str
    password: str


class CreateUserResponse(BaseModel):
    id: str
    name: str


def create_user(req: CreateUserRequest, fake_user_repository: UserRepository) -> CreateUserResponse:
    user = User(id=req.id, name=req.name, password=req.password)
    fake_user_repository.save(user)
    return CreateUserResponse(id=user.id, name=user.name)
