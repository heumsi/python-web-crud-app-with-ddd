from fastapi import FastAPI

from app import users
from app.container import ApplicationContainer


def create_app() -> FastAPI:
    container = ApplicationContainer()
    container.config.from_yaml("config.yaml")

    app_ = FastAPI()
    app_.mount("/users", users.create_app(container.user_container))

    return app_
