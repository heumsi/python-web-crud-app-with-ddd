from app.posts.domain.model import PostBase, Post
from app.posts.service_layer import CRUDBase


class CreatePostRequest(PostBase):
    pass


class CreatePostResponse(Post):
    pass


class CreatePost(CRUDBase):
    def execute(self, req: CreatePostRequest) -> CreatePostResponse:
        with self.uow:
            post = Post(title=req.title, content=req.content, user_id=req.user_id)
            self.post_repository.save(post)
        return CreatePostResponse(**post.dict())
