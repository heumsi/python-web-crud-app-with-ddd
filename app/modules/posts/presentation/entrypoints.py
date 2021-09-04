from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from app.modules.posts import PostContainer
from app.modules.posts.presentation.schemas import (
    CreatePostJsonRequest,
    UpdatePostJSONRequest,
    UpdatePostJSONResponse,
)
from app.modules.posts.service_layer.use_cases.create import CreatePost
from app.modules.posts.service_layer.use_cases.delete import (
    DeletePost,
    DeletePostRequest,
)
from app.modules.posts.service_layer.use_cases.read import (
    ReadPost,
    ReadPostRequest,
    ReadPosts,
    ReadPostsRequest,
)
from app.modules.posts.service_layer.use_cases.update import (
    UpdatePost,
    UpdatePostRequest,
)

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
    json_req: CreatePostJsonRequest,
    service: CreatePost = Depends(Provide[PostContainer.create_post]),
):
    # authorize
    # authorize_user_req = AuthorizeUserRequest(
    #     id=json_req.user_id, password=json_req.user_password
    # )
    # _ = authorize_user_service.execute(authorize_user_req)
    #
    # # do service
    # req = CreatePostRequest(
    #     title=json_req.title, content=json_req.content, user_id=json_req.user_id
    # )
    # res = service.execute(req)
    # return CreatePostJsonResponse(
    #     title=res.title, content=res.content, user_id=res.user_id, id=res.id
    # )
    pass


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
