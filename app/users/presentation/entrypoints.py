from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from app.users.adapters.container import UserContainer
from app.users.service_layer.create import CreateUser, CreateUserRequest
from app.users.service_layer.delete import DeleteUser, DeleteUserRequest
from app.users.service_layer.read import ReadUser, ReadUserRequest, ReadUsers

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
@inject
def get_users(service: ReadUsers = Depends(Provide[UserContainer.read_users])):
    res = service.execute()
    return res.dict()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
@inject
def get_user(
    user_id: str, service: ReadUser = Depends(Provide[UserContainer.read_user])
):
    req = ReadUserRequest(id=user_id)
    res = service.execute(req)
    return res.dict()


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def create_user(
    req: CreateUserRequest,
    service: CreateUser = Depends(Provide[UserContainer.create_user]),
):
    res = service.execute(req)
    return res.dict()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_user(
    user_id: str, service: DeleteUser = Depends(Provide[UserContainer.delete_user])
):
    req = DeleteUserRequest(id=user_id)
    service.execute(req)
    return None
