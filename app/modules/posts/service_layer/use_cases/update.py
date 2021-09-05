from pydantic import BaseModel

from app.modules.common.service_layer.exceptions import UnauthorizedError
from app.modules.posts.domain.model import Post
from app.modules.posts.service_layer.use_cases import CRUDBase


class UpdatePostRequest(BaseModel):
    id: str
    title: str
    content: str
    requested_user_id: str


class UpdatePostResponse(Post):
    id: str
    title: str
    content: str
    user_id: str


class UpdatePost(CRUDBase):
    def execute(self, req: UpdatePostRequest) -> UpdatePostResponse:
        with self.uow:
            post = self.post_repository.find_by_id(req.id)
            if post.user_id != req.requested_user_id:
                raise UnauthorizedError("본인의 게시글만 수정할 수 있습니다.")
            post = Post(id=post.id, title=req.title, content=req.content, user_id=post.user_id)
            post = self.post_repository.save(post)
            self.uow.commit()
        return UpdatePostResponse(**post.dict())
