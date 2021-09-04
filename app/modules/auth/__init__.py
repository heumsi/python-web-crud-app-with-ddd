from fastapi import FastAPI

from app.modules.auth.config import Config
from app.modules.auth.presentation import entrypoints
from app.modules.auth.presentation.container import AuthContainer

# from app.modules.auth.presentation.entrypoints import router
from app.modules.auth.presentation.error_handler import add_error_handler


def create_app(container: AuthContainer) -> FastAPI:
    container.wire(packages=[entrypoints])
    container.config.from_pydantic(Config())
    # container.wire(modules=[post_token])

    app_ = FastAPI()
    app_.include_router(entrypoints.router)
    add_error_handler(app_)
    # add_common_error_handler(app_)

    return app_
