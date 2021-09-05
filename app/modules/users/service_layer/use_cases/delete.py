from pydantic import BaseModel

from app.modules.common.service_layer.exceptions import UnauthorizedError
from app.modules.common.service_layer.unit_of_work import UnitOfWork
from app.modules.users.domain.repository import UserRepository


class DeleteUserRequest(BaseModel):
    id: str
    requested_user_id: str


class DeleteUser:
    def __init__(self, user_repository: UserRepository, uow: UnitOfWork) -> None:
        self._user_repository = user_repository
        self._uow = uow

    def execute(self, req: DeleteUserRequest) -> None:
        with self._uow:
            user = self._user_repository.delete_by_id(req.id)
            if user.id != req.requested_user_id:
                raise UnauthorizedError("본인의 아이디만 삭제할 수 있습니다.")
            self._uow.commit()
