from typing import List

from pydantic import BaseModel

from app.users.domain.repository import UserRepository


class ReadUserRequest(BaseModel):
    id: str


class ReadUserResponse(BaseModel):
    id: str
    name: str


def read_user(req: ReadUserRequest, fake_user_repository: UserRepository) -> ReadUserResponse:
    user = fake_user_repository.find_by_id(req.id)
    return ReadUserResponse(id=user.id, name=user.name)


class ReadUsersResponse(BaseModel):
    items: List[ReadUserResponse]


def read_users(fake_user_repository: UserRepository) -> ReadUsersResponse:
    users = fake_user_repository.find_all()
    return ReadUsersResponse(items=[ReadUserResponse(id=user.id, name=user.name) for user in users])
