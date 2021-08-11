from pydantic import BaseModel

from app.users.domain.repository import UserRepository


class DeleteUserRequest(BaseModel):
    id: str


def delete_user(req: DeleteUserRequest, fake_user_repository: UserRepository) -> None:
    fake_user_repository.delete_by_id(req.id)
