from pydantic import BaseModel

from app.common.service_layer.unit_of_work import UnitOfWork
from app.users.domain.repository import UserRepository


class DeleteUserRequest(BaseModel):
    id: str


class DeleteUser:
    def __init__(self, user_repository: UserRepository, uow: UnitOfWork) -> None:
        self._user_repository = user_repository
        self._uow = uow

    def execute(self, req: DeleteUserRequest) -> None:
        with self._uow:
            self._user_repository.delete_by_id(req.id)
            self._uow.commit()
