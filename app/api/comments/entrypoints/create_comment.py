from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from pydantic import BaseModel

from app.api.common.dependencies import TokenPayload, get_token_payload
from app.modules.comments.service_layer.use_cases.create_comment import CreateComment, CreateCommentRequest
from app.modules.common.service_layer.unit_of_work import UnitOfWork
from app.modules.container import AppContainer


class CreateCommentJSONRequest(BaseModel):
    post_id: str
    content: str


class CreateCommentJSONResponse(BaseModel):
    comment_id: str


@inject
def create_comment(
    json_req: CreateCommentJSONRequest,
    use_case: CreateComment = Depends(Provide[AppContainer.comments.create_comment]),
    token_payload: TokenPayload = Depends(get_token_payload),
    uow: UnitOfWork = Depends(Provide[AppContainer.uow])
) -> CreateCommentJSONResponse:
    req = CreateCommentRequest(user_id=token_payload.user_id, post_id=json_req.post_id, content=json_req.content)
    res = use_case.execute(req, uow=uow)
    return CreateCommentJSONResponse(comment_id=res.comment_id)
