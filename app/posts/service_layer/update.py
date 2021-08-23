from ulid import ULID

from app.posts import Post
from app.posts.service_layer import CRUDBase


class UpdatePostRequest(Post):
    pass


class UpdatePostResponse(Post):
    pass


class UpdatePost(CRUDBase):
    def execute(self, req: UpdatePostRequest) -> UpdatePostResponse:
        with self.uow:
            post = Post(id=req.id, **req.dict(exclude={'id'}))
            self.post_repository.save(post)
        return UpdatePostResponse(**post.dict())