from fastapi import FastAPI

from app.container import ApplicationContainer
from app.infrastructures.persistence import create_tables
from app.modules import auth, posts, users


def create_app() -> FastAPI:
    container = ApplicationContainer()
    container.config.from_yaml("config.yaml")

    create_tables(container.db())

    app_ = FastAPI()
    app_.mount("/users", users.create_app(container.user_container))
    app_.mount("/posts", posts.create_app(container.post_container))
    app_.mount("/auth", auth.create_app(container.auth_container))

    return app_
