from app.modules.common.service_layer.unit_of_work import UnitOfWork
from app.modules.posts.domain.repository import PostRepository


class CRUDBase:
    def __init__(self, post_repository: PostRepository, uow: UnitOfWork) -> None:
        self.post_repository = post_repository
        self.uow = uow
