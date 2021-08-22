from fastapi import FastAPI

from app import users


def create_app() -> FastAPI:
    app_ = FastAPI()
    app_.mount("/users", users.create_app())

    return app_
