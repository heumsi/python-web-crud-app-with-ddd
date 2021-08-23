from pydantic import BaseModel

from app.common.service_layer.unit_of_work import UnitOfWork
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
    def __init__(self, user_repository: UserRepository, uow: UnitOfWork) -> None:
        self._user_repository = user_repository
        self._uow = uow

    def execute(self, req: CreateUserRequest) -> CreateUserResponse:
        user = User(id=req.id, name=req.name, password=req.password)
        with self._uow:
            self._user_repository.save(user)
            self._uow.commit()
        return CreateUserResponse(id=user.id, name=user.name)
