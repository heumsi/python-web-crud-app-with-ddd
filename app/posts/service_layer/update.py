from app.posts.domain.model import Post
from app.posts.service_layer import CRUDBase


class UpdatePostRequest(Post):
    pass


class UpdatePostResponse(Post):
    pass


class UpdatePost(CRUDBase):
    def execute(self, req: UpdatePostRequest) -> UpdatePostResponse:
        with self.uow:
            post = Post(id=req.id, **req.dict(exclude={"id"}))
            self.post_repository.save(post)
            self.uow.commit()
        return UpdatePostResponse(**post.dict())
