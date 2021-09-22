from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from app.api.common.dependencies import TokenPayload, get_token_payload
from app.api.posts.schemas import (
    CreatePostJsonRequest,
    CreatePostJsonResponse,
    UpdatePostJSONRequest,
    UpdatePostJSONResponse,
)
from app.modules.container import AppContainer
from app.modules.posts.service_layer.use_cases.command.create import (
    CreatePost,
    CreatePostRequest,
)
from app.modules.posts.service_layer.use_cases.command.delete import (
    DeletePost,
    DeletePostRequest,
)
from app.modules.posts.service_layer.use_cases.command.update import (
    UpdatePost,
    UpdatePostRequest,
)
from app.modules.posts.service_layer.use_cases.query.read import (
    ReadPost,
    ReadPostRequest,
    ReadPosts,
    ReadPostsRequest,
)

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
@inject
def get_posts(
    user_id: str = None,
    service: ReadPosts = Depends(Provide[AppContainer.posts.read_posts]),
):
    req = ReadPostsRequest(user_id=user_id)
    res = service.execute(req)
    return res.dict()


@router.get("/{post_id}", status_code=status.HTTP_200_OK)
@inject
def get_post(
    post_id: str, service: ReadPost = Depends(Provide[AppContainer.posts.read_post])
):
    req = ReadPostRequest(id=post_id)
    res = service.execute(req)
    return res.dict()


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def create_post(
    json_req: CreatePostJsonRequest,
    service: CreatePost = Depends(Provide[AppContainer.posts.create_post]),
    token_payload: TokenPayload = Depends(get_token_payload),
):
    req = CreatePostRequest(
        title=json_req.title, content=json_req.content, user_id=token_payload.user_id
    )
    res = service.execute(req)
    return CreatePostJsonResponse(
        title=res.title, content=res.content, user_id=res.user_id, id=res.id
    )


@router.put("/{post_id}", status_code=status.HTTP_200_OK)
@inject
def update_post(
    post_id: str,
    json_req: UpdatePostJSONRequest,
    service: UpdatePost = Depends(Provide[AppContainer.posts.update_post]),
    token_payload: TokenPayload = Depends(get_token_payload),
):
    req = UpdatePostRequest(
        id=post_id,
        title=json_req.title,
        content=json_req.content,
        requested_user_id=token_payload.user_id,
    )
    res = service.execute(req)
    return UpdatePostJSONResponse(**res.dict())


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_post(
    post_id: str,
    service: DeletePost = Depends(Provide[AppContainer.posts.delete_post]),
    token_payload: TokenPayload = Depends(get_token_payload),
):
    req = DeletePostRequest(id=post_id, requested_user_id=token_payload.user_id)
    service.execute(req)
    return None
