from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.users import UserContainer
from app.users.service_layer.unit_of_work import DatasetUnitOfWork


class ApplicationContainer(DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database, url=config.db.url)
    uow = providers.Singleton(DatasetUnitOfWork, db=db)

    user_container = providers.Container(
        UserContainer,
        db=db,
        uow=uow,
    )