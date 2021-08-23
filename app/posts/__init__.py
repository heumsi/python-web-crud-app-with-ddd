import uvicorn
from fastapi import FastAPI

from app.posts.domain.model import Post


def create_app() -> FastAPI:
    # container = UserContainer()
    # container.wire(modules=[entrypoints])

    # db = container.database()
    # create_tables(db)

    app_ = FastAPI()
    # app_.include_router(entrypoints.router)
    # add_error_handler(app_)

    return app_


if __name__ == "__main__":
    app_ = create_app()
    uvicorn.run(app_, host="0.0.0.0", port=8000)
