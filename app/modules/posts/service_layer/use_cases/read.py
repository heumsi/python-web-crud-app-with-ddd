from typing import List

from pydantic import BaseModel

from app.modules.posts.domain.model import Post
from app.modules.posts.service_layer import CRUDBase
from app.modules.posts.service_layer.exceptions import PostNotFoundError


class ReadPostRequest(BaseModel):
    id: str


class ReadPostResponse(Post):
    pass


class ReadPost(CRUDBase):
    def execute(self, req: ReadPostRequest) -> ReadPostResponse:
        with self.uow:
            post = self.post_repository.find_by_id(req.id)
            if not post:
                raise PostNotFoundError("게시글을 찾을 수 없습니다.")
        return ReadPostResponse(**post.dict())


class ReadPostsRequest(BaseModel):
    user_id: str = None


class ReadPostsResponse(BaseModel):
    items: List[ReadPostResponse]


class ReadPosts(CRUDBase):
    def execute(self, req: ReadPostsRequest) -> ReadPostsResponse:
        if not req.user_id:
            with self.uow:
                posts = self.post_repository.find_all()
        else:
            with self.uow:
                posts = self.post_repository.find_by_user_id(req.user_id)
        return ReadPostsResponse(
            items=[ReadPostResponse(**post.dict()) for post in posts]
        )
