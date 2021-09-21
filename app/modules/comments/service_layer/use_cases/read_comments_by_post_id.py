# from typing import List
#
# from pydantic import BaseModel
#
# from app.modules.comment.service_layer.ports.repository import CommentRepository
# from app.modules.comment.service_layer.use_cases.read_comment import ReadCommentResponse
# from app.modules.common.service_layer.unit_of_work import UnitOfWork
#
#
# class ReadCommentsByPostIdRequest(BaseModel):
#     post_id: str
#
#
# class ReadCommentsByPostIdResponse(BaseModel):
#     items: List[ReadCommentResponse]
#
#
# class ReadCommentsByPostId:
#     def __init__(self, comment_repository: CommentRepository) -> None:
#         self._comment_repository =comment_repository
#
#     def execute(self, req: ReadCommentsByPostIdRequest, uow: UnitOfWork) -> ReadCommentsByPostIdResponse:
#         with uow:
#             comments = self._comment_repository.find_all_by_post_id(req.post_id)
#         return ReadCommentsByPostIdResponse(
#             items=[ReadCommentResponse(
#                 comment_id=comment.id,
#                 content=comment.content,
#                 user_id=comment.user_id,
#                 post_id=comment.post_id
#             ) for comment in comments]
#         )
