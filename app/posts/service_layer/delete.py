from pydantic import BaseModel

from app.posts.service_layer import CRUDBase


class DeletePostRequest(BaseModel):
    id: str


class DeletePost(CRUDBase):
    def execute(self, req: DeletePostRequest) -> None:
        with self.uow:
            self.post_repository.delete_by_id(req.id)
