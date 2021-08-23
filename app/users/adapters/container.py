from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.users.adapters.repository import DatasetUserRepository
from app.users.service_layer.create import CreateUser
from app.users.service_layer.delete import DeleteUser
from app.users.service_layer.read import ReadUser, ReadUsers
from app.common.service_layer.unit_of_work import DatasetUnitOfWork


class UserContainer(DeclarativeContainer):
    # repositories
    db = providers.Dependency()
    uow = providers.Dependency()
    user_repository = providers.Singleton(DatasetUserRepository, db=db)

    # services
    read_user = providers.Singleton(ReadUser, user_repository=user_repository, uow=uow)
    read_users = providers.Singleton(ReadUsers, user_repository=user_repository, uow=uow)
    create_user = providers.Singleton(CreateUser, user_repository=user_repository, uow=uow)
    delete_user = providers.Singleton(DeleteUser, user_repository=user_repository, uow=uow)
