from pydantic import BaseModel

from app.users.domain.repository import UserRepository


class DeleteUserRequest(BaseModel):
    id: str


class DeleteUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, req: DeleteUserRequest) -> None:
        self.user_repository.delete_by_id(req.id)
