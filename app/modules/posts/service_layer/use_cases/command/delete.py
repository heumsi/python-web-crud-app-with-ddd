from typing import Optional

from pydantic import BaseModel

from app.modules.common.service_layer.exceptions import UnauthorizedError
from app.modules.common.service_layer.unit_of_work import UnitOfWork
from app.modules.posts.service_layer.use_cases import CRUDBase


class DeletePostRequest(BaseModel):
    id: str
    requested_user_id: str


class DeletePost(CRUDBase):
    def execute(self, req: DeletePostRequest) -> None:
        with self.uow:
            post = self.post_repository.delete_by_id(req.id)
            if post.user_id != req.requested_user_id:
                raise UnauthorizedError("본인의 게시글만 삭제할 수 있습니다.")
            self.uow.commit()


class DeletePostsByUserIdRequest(BaseModel):
    user_id: str
    requested_user_id: str


class DeletePostsByUserId(CRUDBase):
    def execute(
        self, req: DeletePostsByUserIdRequest, uow: Optional[UnitOfWork]
    ) -> None:
        if not uow:
            uow = self.uow

        with uow:
            if req.user_id != req.requested_user_id:
                raise UnauthorizedError("본인의 게시글만 삭제할 수 있습니다.")
            self.post_repository.delete_all_by_user_id(req.user_id)
            uow.commit()
