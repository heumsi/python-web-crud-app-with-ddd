from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Header
from pydantic import BaseModel, Required

from app.modules.auth.presentation.container import AuthContainer
from app.modules.auth.service_layer.use_cases.get_token_payload import (
    GetTokenPayload,
    GetTokenPayloadRequest,
)


class GetTokenJSONReponse(BaseModel):
    user_id: str


@inject
def get_token_payload(
    service: GetTokenPayload = Depends(Provide[AuthContainer.get_token_payload]),
    token: str = Header(Required),
):
    req = GetTokenPayloadRequest(token=token)
    res = service.execute(req)
    return GetTokenJSONReponse(**res.dict())
