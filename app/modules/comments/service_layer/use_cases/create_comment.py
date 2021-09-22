from pydantic import BaseModel

from app.modules.comments.domain.model import Comment
from app.modules.comments.service_layer.ports.repository import CommentRepository
from app.modules.common.service_layer.unit_of_work import UnitOfWork


class CreateCommentRequest(BaseModel):
    user_id: str
    post_id: str
    content: str


class CreateCommentResponse(BaseModel):
    comment_id: str


class CreateComment:
    def __init__(self, comment_repository: CommentRepository) -> None:
        self._comment_repository = comment_repository

    def execute(
        self, req: CreateCommentRequest, uow: UnitOfWork
    ) -> CreateCommentResponse:
        with uow:
            comment = Comment(
                user_id=req.user_id, post_id=req.post_id, content=req.content
            )
            self._comment_repository.save(comment)
            uow.commit()
        return CreateCommentResponse(comment_id=comment.id)
