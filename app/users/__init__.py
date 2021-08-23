from fastapi import FastAPI

from app.users.adapters.container import UserContainer
from app.users.adapters.repository import create_tables
from app.users.presentation import entrypoints
from app.users.presentation.error_handler import add_error_handler


def create_app(container: UserContainer) -> FastAPI:
    container.wire(modules=[entrypoints])
    create_tables(container.db())

    app_ = FastAPI()
    app_.include_router(entrypoints.router)
    add_error_handler(app_)

    return app_
