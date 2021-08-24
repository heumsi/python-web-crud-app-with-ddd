from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.common.service_layer.unit_of_work import DatasetUnitOfWork
from app.posts import PostContainer
from app.users import UserContainer


class ApplicationContainer(DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database, url=config.db.url)
    uow = providers.Singleton(DatasetUnitOfWork, db=db)

    user_container = providers.Container(UserContainer, db=db, uow=uow)
    post_container = providers.Container(PostContainer, db=db, uow=uow, authorize_user=user_container.authorize_user)
