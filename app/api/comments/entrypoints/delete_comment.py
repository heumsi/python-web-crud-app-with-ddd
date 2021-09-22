from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from pydantic import BaseModel

from app.api.common.dependencies import TokenPayload, get_token_payload
from app.modules.comments.service_layer.use_cases.delete_comment import (
    DeleteComment,
    DeleteCommentRequest,
)
from app.modules.common.service_layer.unit_of_work import UnitOfWork
from app.modules.container import AppContainer


class DeleteCommentJSONResponse(BaseModel):
    comment_id: str


@inject
def delete_comment(
    comment_id: str,
    use_case: DeleteComment = Depends(Provide[AppContainer.comments.delete_comment]),
    token_payload: TokenPayload = Depends(get_token_payload),
    uow: UnitOfWork = Depends(Provide[AppContainer.uow]),
) -> None:
    req = DeleteCommentRequest(
        comment_id=comment_id, requested_user_id=token_payload.user_id
    )
    use_case.execute(req, uow=uow)
