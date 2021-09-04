from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.modules.users.adapters.repository import DatasetUserRepository
from app.modules.users.service_layer.use_cases.create import CreateUser
from app.modules.users.service_layer.use_cases.delete import DeleteUser
from app.modules.users.service_layer.use_cases.read import ReadUser, ReadUsers


class UserContainer(DeclarativeContainer):
    # repositories
    db = providers.Dependency()
    uow = providers.Dependency()
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
        DeleteUser, user_repository=user_repository, uow=uow
    )
