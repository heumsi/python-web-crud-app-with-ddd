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


class CreateUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, req: CreateUserRequest) -> CreateUserResponse:
        user = User(id=req.id, name=req.name, password=req.password)
        self.user_repository.save(user)
        return CreateUserResponse(id=user.id, name=user.name)
