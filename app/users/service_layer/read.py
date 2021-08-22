from typing import List

from pydantic import BaseModel

from app.users.domain.exceptions import UserNotFoundError
from app.users.domain.repository import UserRepository


class ReadUserRequest(BaseModel):
    id: str


class ReadUserResponse(BaseModel):
    id: str
    name: str


class ReadUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, req: ReadUserRequest) -> ReadUserResponse:
        user = self.user_repository.find_by_id(req.id)
        if not user:
            raise UserNotFoundError("유저를 찾을 수 없습니다")
        return ReadUserResponse(id=user.id, name=user.name)


class ReadUsersResponse(BaseModel):
    items: List[ReadUserResponse]


class ReadUsers:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self) -> ReadUsersResponse:
        users = self.user_repository.find_all()
        return ReadUsersResponse(
            items=[ReadUserResponse(id=user.id, name=user.name) for user in users]
        )
