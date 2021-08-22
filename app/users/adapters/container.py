from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.users.adapters.repository import DatasetUserRepository
from app.users.service_layer.create import CreateUser
from app.users.service_layer.delete import DeleteUser
from app.users.service_layer.read import ReadUser, ReadUsers
from app.users.service_layer.unit_of_work import DatasetUnitOfWork


class UserContainer(DeclarativeContainer):
    # repositories
    db = providers.Singleton(Database, url="sqlite://")
    uow = providers.Singleton(DatasetUnitOfWork, db=db)
    user_repository = providers.Singleton(DatasetUserRepository, db=db)

    # services
    read_user = providers.Singleton(ReadUser, user_repository)
    read_users = providers.Singleton(ReadUsers, user_repository)
    create_user = providers.Singleton(CreateUser, user_repository)
    delete_user = providers.Singleton(DeleteUser, user_repository)
