from pydantic import BaseModel

from app.modules.common.service_layer.unit_of_work import UnitOfWork
from app.modules.users.domain.model import User
from app.modules.users.domain.repository import UserRepository


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
