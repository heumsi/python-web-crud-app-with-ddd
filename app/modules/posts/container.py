from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.modules.posts.adapters.repository import DatasetPostRepository
from app.modules.posts.service_layer.use_cases.create import CreatePost
from app.modules.posts.service_layer.use_cases.delete import (
    DeletePost,
    DeletePostsByUserId,
)
from app.modules.posts.service_layer.use_cases.read import ReadPost, ReadPosts
from app.modules.posts.service_layer.use_cases.update import UpdatePost


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
    delete_posts_by_user_id = providers.Singleton(
        DeletePostsByUserId, post_repository=post_repository, uow=uow
    )
