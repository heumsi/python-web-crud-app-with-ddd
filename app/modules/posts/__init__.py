from fastapi import FastAPI

from app.modules.common.presentation.error_handler import add_common_error_handler
from app.modules.posts.adapters.container import PostContainer
from app.modules.posts.presentation import entrypoints
from app.modules.posts.presentation.error_handler import add_error_handler


def create_app(container: PostContainer) -> FastAPI:
    container.wire(modules=[entrypoints])

    app_ = FastAPI()
    app_.include_router(entrypoints.router)
    add_error_handler(app_)
    add_common_error_handler(app_)

    return app_
