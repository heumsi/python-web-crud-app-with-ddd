from fastapi import FastAPI

from app import posts, users
from app.container import ApplicationContainer


def create_app() -> FastAPI:
    container = ApplicationContainer()
    container.config.from_yaml("config.yaml")

    app_ = FastAPI()
    app_.mount("/users", users.create_app(container.user_container))
    app_.mount("/posts", posts.create_app(container.post_container))

    return app_
