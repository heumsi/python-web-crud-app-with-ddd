from typing import Optional

from pydantic import BaseModel

from app.modules.common.service_layer.exceptions import UnauthorizedError
from app.modules.common.service_layer.unit_of_work import UnitOfWork
from app.modules.posts.service_layer.use_cases.delete import (
    DeletePost,
    DeletePostsByUserId,
    DeletePostsByUserIdRequest,
)
from app.modules.users.domain.repository import UserRepository
from app.modules.users.service_layer.exceptions import UserNotFoundError


class DeleteUserRequest(BaseModel):
    id: str
    requested_user_id: str


class DeleteUser:
    def __init__(
        self,
        user_repository: UserRepository,
        uow: UnitOfWork,
        delete_posts_by_user_id: DeletePostsByUserId,
    ) -> None:
        self._user_repository = user_repository
        self._delete_posts_by_user_id = delete_posts_by_user_id
        self._uow = uow

    def execute(self, req: DeleteUserRequest, uow: Optional[UnitOfWork] = None) -> None:
        if not uow:
            uow = self._uow

        with uow:
            user = self._user_repository.delete_by_id(req.id)
            if not user:
                raise UserNotFoundError("삭제할 아이디를 찾을 수 없습니다.")
            if user.id != req.requested_user_id:
                raise UnauthorizedError("본인의 아이디만 삭제할 수 있습니다.")

            delete_posts_by_user_id_req = DeletePostsByUserIdRequest(
                user_id=req.id, requested_user_id=req.requested_user_id
            )
            self._delete_posts_by_user_id.execute(delete_posts_by_user_id_req, uow=uow)
            uow.commit()
