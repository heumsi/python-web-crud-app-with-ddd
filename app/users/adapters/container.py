from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.users.adapters.repository import DatasetUserRepository
from app.users.service_layer.create import CreateUser
from app.users.service_layer.delete import DeleteUser
from app.users.service_layer.read import ReadUser, ReadUsers


class UserContainer(DeclarativeContainer):
    # repositories
    database = providers.Singleton(Database, url="sqlite://")
    user_repository = providers.Singleton(DatasetUserRepository, db=database)

    # services
    read_user = providers.Singleton(ReadUser, user_repository)
    read_users = providers.Singleton(ReadUsers, user_repository)
    create_user = providers.Singleton(CreateUser, user_repository)
    delete_user = providers.Singleton(DeleteUser, user_repository)
