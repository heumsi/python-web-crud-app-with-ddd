from fastapi import FastAPI

from app.api import auth, comments, common, posts, users
from app.modules.container import AppContainer


def _add_routers(app_: FastAPI) -> None:
    app_.include_router(auth.entrypoints.router, prefix="/auth")
    app_.include_router(users.entrypoints.router, prefix="/users")
    app_.include_router(posts.entrypoints.router, prefix="/posts")
    app_.include_router(comments.entrypoints.router, prefix="/comments")


def _add_error_handler(app_: FastAPI) -> None:
    auth.add_error_handler(app_)
    users.add_error_handler(app_)
    posts.add_error_handler(app_)
    common.add_error_handler(app_)
    comments.add_error_handler(app_)


def create_app(container: AppContainer) -> FastAPI:
    app_ = FastAPI()
    _add_routers(app_)
    _add_error_handler(app_)
    return app_
