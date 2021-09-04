from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.modules.auth import AuthContainer
from app.modules.common.service_layer.unit_of_work import DatasetUnitOfWork
from app.modules.posts import PostContainer
from app.modules.users import UserContainer


class ApplicationContainer(DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database, url=config.db.url)
    uow = providers.Singleton(DatasetUnitOfWork, db=db)

    user_container = providers.Container(UserContainer, db=db, uow=uow)
    post_container = providers.Container(PostContainer, db=db, uow=uow)
    auth_container = providers.Container(AuthContainer, db=db, uow=uow)
