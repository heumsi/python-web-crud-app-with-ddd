from dataset import Database
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.modules.auth.container import AuthContainer
from app.modules.comments.conatiner import CommentContainer
from app.modules.common.adapters.unit_of_work import DatasetUnitOfWork
from app.modules.posts.container import PostContainer
from app.modules.users.container import UserContainer


class AppContainer(DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database, url=config.db.url)
    uow = providers.Singleton(DatasetUnitOfWork, db=db)

    posts = providers.Container(PostContainer, db=db, uow=uow)
    users = providers.Container(UserContainer, db=db, uow=uow, posts=posts)
    auth = providers.Container(AuthContainer, config=config.auth, db=db, uow=uow)
    comments = providers.Container(CommentContainer, db=db, uow=uow)
