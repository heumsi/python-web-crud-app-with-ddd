from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.modules.comments.adapters.repository import DatasetCommentRepository
from app.modules.comments.service_layer.use_cases.create_comment import CreateComment
from app.modules.comments.service_layer.use_cases.delete_comment import DeleteComment

# from app.modules.comments.service_layer.use_cases.update_comment import UpdateComment
from app.modules.common.adapters.unit_of_work import DatasetUnitOfWork


class CommentContainer(DeclarativeContainer):
    # dependency
    db = providers.Dependency(Database)
    uow = providers.Dependency(DatasetUnitOfWork)

    # repositories
    comment_repository = providers.Singleton(DatasetCommentRepository, db=db)

    # use_cases
    create_comment = providers.Singleton(
        CreateComment, comment_repository=comment_repository
    )
    delete_comment = providers.Singleton(
        DeleteComment, comment_repository=comment_repository
    )
    # update_comment = providers.Singleton(UpdateComment, comment_repository=comment_repository)
