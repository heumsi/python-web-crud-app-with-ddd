from fastapi import FastAPI

from app.posts.adapters.container import PostContainer
from app.posts.adapters.repository import create_tables
from app.posts.presentation import entrypoints
from app.posts.presentation.error_handler import add_error_handler


def create_app(container: PostContainer) -> FastAPI:
    container.wire(modules=[entrypoints])
    create_tables(container.db())

    app_ = FastAPI()
    app_.include_router(entrypoints.router)
    add_error_handler(app_)

    return app_
