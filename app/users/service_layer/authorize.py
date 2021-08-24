from typing import Optional

from pydantic import BaseModel

from app.common.service_layer.unit_of_work import UnitOfWork
from app.common.domain.exceptions import AuthroizeError
from app.users.domain.repository import UserRepository


class AuthorizeUserRequest(BaseModel):
    id: str
    password: str


class AuthorizeUserResponse(BaseModel):
    id: str
    name: str


class AuthorizeUser:
    def __init__(self, user_repository: UserRepository, uow: UnitOfWork):
        self._user_repository = user_repository
        self._uow = uow

    def execute(self, req: AuthorizeUserRequest) -> AuthorizeUserResponse:
        with self._uow:
            user = self._user_repository.find_by_id(req.id)
        if not user:
            raise AuthroizeError("등록된 유저가 아닙니다.")
        if user.password != req.password:
            raise AuthroizeError("패스워드가 다릅니다.")
        return AuthorizeUserResponse(id=user.id, name=user.name)
