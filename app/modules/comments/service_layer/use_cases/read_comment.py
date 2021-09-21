# from pydantic import BaseModel
#
# from app.modules.comment.service_layer.exceptions import CommentNotFoundError
# from app.modules.comment.service_layer.ports.repository import CommentRepository
# from app.modules.common.service_layer.unit_of_work import UnitOfWork
#
#
# class ReadCommentRequest(BaseModel):
#     comment_id: str
#
# class ReadCommentResponse(BaseModel):
#     comment_id: str
#     content: str
#     user_id: str
#     post_id: str
#
# class ReadComment:
#     def __init__(self, comment_repository: CommentRepository) -> None:
#         self._comment_repository = comment_repository
#
#     def execute(self, req: ReadCommentRequest, uow: UnitOfWork) -> ReadCommentResponse:
#         with uow:
#             comment = self._comment_repository.find_by_id(comment_id=req.comment_id)
#             if not comment:
#                 raise CommentNotFoundError("해당하는 댓글이 없습니다.")
#         return ReadCommentResponse(comment_id=comment.id, content=comment.content, user_id=comment.user_id, post_id=comment.post_id)