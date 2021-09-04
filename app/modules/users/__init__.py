from fastapi import FastAPI

from app.modules.common.presentation.error_handler import add_common_error_handler
from app.modules.users.adapters.container import UserContainer
from app.modules.users.presentation import entrypoints
from app.modules.users.presentation.error_handler import add_error_handler


def create_app(container: UserContainer) -> FastAPI:
    container.wire(modules=[entrypoints])

    app_ = FastAPI()
    app_.include_router(entrypoints.router)
    add_error_handler(app_)
    add_common_error_handler(app_)

    return app_
