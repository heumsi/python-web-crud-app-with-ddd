from typing import List

from pydantic import BaseModel

from app.users.domain.exceptions import UserNotFoundError
from app.users.domain.repository import UserRepository
from app.common.service_layer.unit_of_work import UnitOfWork


class ReadUserRequest(BaseModel):
    id: str


class ReadUserResponse(BaseModel):
    id: str
    name: str


class ReadUser:
    def __init__(self, user_repository: UserRepository, uow: UnitOfWork) -> None:
        self._user_repository = user_repository
        self._uow = uow

    def execute(self, req: ReadUserRequest) -> ReadUserResponse:
        with self._uow:
            user = self._user_repository.find_by_id(req.id)
        if not user:
            raise UserNotFoundError("유저를 찾을 수 없습니다")
        return ReadUserResponse(id=user.id, name=user.name)


class ReadUsersResponse(BaseModel):
    items: List[ReadUserResponse]


class ReadUsers:
    def __init__(self, user_repository: UserRepository, uow: UnitOfWork) -> None:
        self._user_repository = user_repository
        self._uow = uow

    def execute(self) -> ReadUsersResponse:
        with self._uow:
            users = self._user_repository.find_all()
        return ReadUsersResponse(
            items=[ReadUserResponse(id=user.id, name=user.name) for user in users]
        )
