from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from app.api.common.dependencies import TokenPayload, get_token_payload
from app.modules.container import AppContainer
from app.modules.posts.service_layer.use_cases.delete import DeletePostsByUserId
from app.modules.users.service_layer.use_cases.create import (
    CreateUser,
    CreateUserRequest,
)
from app.modules.users.service_layer.use_cases.delete import (
    DeleteUser,
    DeleteUserRequest,
)
from app.modules.users.service_layer.use_cases.read import (
    ReadUser,
    ReadUserRequest,
    ReadUsers,
)

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
@inject
def get_users(service: ReadUsers = Depends(Provide[AppContainer.users.read_users])):
    res = service.execute()
    return res.dict()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
@inject
def get_user(
    user_id: str, service: ReadUser = Depends(Provide[AppContainer.users.read_user])
):
    req = ReadUserRequest(id=user_id)
    res = service.execute(req)
    return res.dict()


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def create_user(
    json_req: CreateUserRequest,
    service: CreateUser = Depends(Provide[AppContainer.users.create_user]),
):
    res = service.execute(json_req)
    return res.dict()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_user(
    user_id: str,
    service: DeleteUser = Depends(Provide[AppContainer.users.delete_user]),
    token_payload: TokenPayload = Depends(get_token_payload),
):
    req = DeleteUserRequest(id=user_id, requested_user_id=token_payload.user_id)
    service.execute(req)
    return None
