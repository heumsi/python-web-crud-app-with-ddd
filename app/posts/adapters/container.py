from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.posts.adapters.repository import DatasetPostRepository
from app.posts.service_layer.create import CreatePost
from app.posts.service_layer.delete import DeletePost
from app.posts.service_layer.read import ReadPost, ReadPosts
from app.posts.service_layer.update import UpdatePost
from app.users.service_layer.authorize import AuthorizeUser


class PostContainer(DeclarativeContainer):
    # repositories
    db = providers.Dependency()
    uow = providers.Dependency()
    post_repository = providers.Singleton(DatasetPostRepository, db=db)

    # services
    read_post = providers.Singleton(ReadPost, post_repository=post_repository, uow=uow)
    read_posts = providers.Singleton(
        ReadPosts, post_repository=post_repository, uow=uow
    )
    create_post = providers.Singleton(
        CreatePost, post_repository=post_repository, uow=uow
    )
    update_post = providers.Singleton(
        UpdatePost, post_repository=post_repository, uow=uow
    )
    delete_post = providers.Singleton(
        DeletePost, post_repository=post_repository, uow=uow
    )

    # other aggregates
    authorize_user: AuthorizeUser = providers.Dependency()
