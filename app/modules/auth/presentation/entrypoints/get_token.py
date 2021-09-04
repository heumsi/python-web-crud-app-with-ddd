from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from pydantic import BaseModel

from app.modules.auth.presentation.container import AuthContainer
from app.modules.auth.service_layer.use_cases.get_token import GetToken, GetTokenRequest


class GetTokenJSONRequest(BaseModel):
    user_id: str
    user_password: str


class GetTokenJSONReponse(BaseModel):
    token: str


@inject
def get_token(
    json_req: GetTokenJSONRequest,
    service: GetToken = Depends(Provide[AuthContainer.get_token]),
):
    req = GetTokenRequest(user_id=json_req.user_id, user_pasword=json_req.user_password)
    res = service.execute(req)
    return GetTokenJSONReponse(token=res.token)
