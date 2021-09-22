from app.modules.posts.domain.model import Post, PostBase
from app.modules.posts.service_layer.use_cases import CRUDBase


class CreatePostRequest(PostBase):
    pass


class CreatePostResponse(Post):
    pass


class CreatePost(CRUDBase):
    def execute(self, req: CreatePostRequest) -> CreatePostResponse:
        with self.uow:
            post = Post(title=req.title, content=req.content, user_id=req.user_id)
            self.post_repository.save(post)
            self.uow.commit()
        return CreatePostResponse(**post.dict())
