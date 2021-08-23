from typing import List

from pydantic import BaseModel

from app.posts import Post
from app.posts.service_layer import CRUDBase


class ReadPostByPostIdRequest(BaseModel):
    id: str


class ReadPostResponse(Post):
    pass


class ReadPostByPostId(CRUDBase):
    def execute(self, req: ReadPostByPostIdRequest) -> ReadPostResponse:
        with self.uow:
            post = self.post_repository.find_by_id(req.id)
        return ReadPostResponse(**post.dict())


class ReadPostsResponse(BaseModel):
    items: List[ReadPostResponse]


class ReadPosts(CRUDBase):
    def execute(self) -> ReadPostsResponse:
        with self.uow:
            posts = self.post_repository.find_all()
        return ReadPostsResponse(
            items=[ReadPostResponse(**post.dict()) for post in posts]
        )


class ReadPostsByUserIdRequest(BaseModel):
    user_id: str


class ReadPostsByUserId(CRUDBase):
    def execute(self, req: ReadPostsByUserIdRequest) -> ReadPostsResponse:
        with self.uow:
            posts = self.post_repository.find_by_user_id(req.user_id)
        return ReadPostsResponse(
            items=[ReadPostResponse(**post.dict()) for post in posts]
        )
