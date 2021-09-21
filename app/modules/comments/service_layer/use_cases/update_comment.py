# from pydantic import BaseModel
#
# from app.modules.comments.domain.model import Comment
# from app.modules.comments.service_layer.ports.repository import CommentRepository
# from app.modules.common.service_layer.unit_of_work import UnitOfWork
#
#
# class UpdateCommentRequest(BaseModel):
#     comment_id: str
#     content: str
#     user_id: str
#     post_id: str
#
#
# class UpdateCommentResponse(BaseModel):
#     comment_id: str
#
#
# class UpdateComment:
#     def __init__(self, comment_repository: CommentRepository) -> None:
#         self._comment_repository = comment_repository
#
#     def execute(self, req: UpdateCommentRequest, uow: UnitOfWork) -> UpdateCommentResponse:
#         with uow:
#             comment = Comment(id=req.comment_id, user_id=req.user_id, post_id=req.post_id, content=req.content)
#             self._comment_repository.save(comment)
#             uow.commit()
#         return UpdateCommentResponse(comment_id=comment.id)
