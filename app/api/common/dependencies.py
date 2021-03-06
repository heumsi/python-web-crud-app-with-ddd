from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Header
from pydantic import BaseModel, Required

from app.modules.auth.service_layer.use_cases.get_token_payload import (
    GetTokenPayload,
    GetTokenPayloadRequest,
)
from app.modules.container import AppContainer


class TokenPayload(BaseModel):
    user_id: str


@inject
def get_token_payload(
    token: str = Header(Required),
    service: GetTokenPayload = Depends(Provide[AppContainer.auth.get_token_payload]),
) -> TokenPayload:
    req = GetTokenPayloadRequest(token=token)
    res = service.execute(req)
    return TokenPayload(user_id=res.user_id)
