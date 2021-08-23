from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from app.posts.adapters.container import PostContainer
from app.posts.presentation.schemas import UpdatePostJSONRequest, UpdatePostJSONResponse
from app.posts.service_layer.create import CreatePost, CreatePostRequest
from app.posts.service_layer.delete import DeletePost, DeletePostRequest
from app.posts.service_layer.read import (
    ReadPost,
    ReadPostRequest,
    ReadPosts,
    ReadPostsRequest,
)
from app.posts.service_layer.update import UpdatePost, UpdatePostRequest

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
@inject
def get_posts(
    user_id: str = None, service: ReadPosts = Depends(Provide[PostContainer.read_posts])
):
    req = ReadPostsRequest(user_id=user_id)
    res = service.execute(req)
    return res.dict()


@router.get("/{post_id}", status_code=status.HTTP_200_OK)
@inject
def get_post(
    post_id: str, service: ReadPost = Depends(Provide[PostContainer.read_post])
):
    req = ReadPostRequest(id=post_id)
    res = service.execute(req)
    return res.dict()


@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
def create_post(
    req: CreatePostRequest,
    service: CreatePost = Depends(Provide[PostContainer.create_post]),
):
    res = service.execute(req)
    return res.dict()


@router.put("/{post_id}", status_code=status.HTTP_200_OK)
@inject
def update_post(
    post_id: str,
    req: UpdatePostJSONRequest,
    service: UpdatePost = Depends(Provide[PostContainer.update_post]),
):
    req = UpdatePostRequest(id=post_id, **req.dict())
    res = service.execute(req)
    return UpdatePostJSONResponse(**res.dict())


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_post(
    post_id: str, service: DeletePost = Depends(Provide[PostContainer.delete_post])
):
    req = DeletePostRequest(id=post_id)
    service.execute(req)
    return None
