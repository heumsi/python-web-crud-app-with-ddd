from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.modules.common.adapters.unit_of_work import DatasetUnitOfWork
from app.modules.posts.container import PostContainer
from app.modules.users.adapters.repository import DatasetUserRepository
from app.modules.users.service_layer.use_cases.create import CreateUser
from app.modules.users.service_layer.use_cases.delete import DeleteUser
from app.modules.users.service_layer.use_cases.read import ReadUser, ReadUsers


class UserContainer(DeclarativeContainer):
    # dependency
    posts = providers.DependenciesContainer()
    db = providers.Dependency(Database)
    uow = providers.Dependency(DatasetUnitOfWork)

    # repositories
    user_repository = providers.Singleton(DatasetUserRepository, db=db)

    # services
    read_user = providers.Singleton(ReadUser, user_repository=user_repository, uow=uow)
    read_users = providers.Singleton(
        ReadUsers, user_repository=user_repository, uow=uow
    )
    create_user = providers.Singleton(
        CreateUser, user_repository=user_repository, uow=uow
    )
    delete_user = providers.Singleton(
        DeleteUser,
        user_repository=user_repository,
        uow=uow,
        delete_posts_by_user_id=posts.delete_posts_by_user_id,
    )
