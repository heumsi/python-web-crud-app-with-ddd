from pydantic import BaseModel

from app.modules.comments.service_layer.exceptions import CommentNotFoundError
from app.modules.comments.service_layer.ports.repository import CommentRepository
from app.modules.common.service_layer.exceptions import UnauthorizedError
from app.modules.common.service_layer.unit_of_work import UnitOfWork


class DeleteCommentRequest(BaseModel):
    comment_id: str
    requested_user_id: str


class DeleteComment:
    def __init__(self, comment_repository: CommentRepository) -> None:
        self._comment_repository = comment_repository

    def execute(self, req: DeleteCommentRequest, uow: UnitOfWork) -> None:
        with uow:
            comment = self._comment_repository.find_by_id(comment_id=req.comment_id)
            if not comment:
                raise CommentNotFoundError("존재하지 않는 댓글입니다")
            if req.requested_user_id != comment.user_id:
                raise UnauthorizedError("본인의 댓글만 삭제할 수 있습니다.")
            self._comment_repository.delete_by_id(comment_id=req.comment_id)
            uow.commit()
