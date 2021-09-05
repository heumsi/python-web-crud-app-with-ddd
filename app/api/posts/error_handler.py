from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.modules.posts.service_layer.exceptions import PostNotFoundError


def add_error_handler(app: FastAPI) -> None:
    @app.exception_handler(PostNotFoundError)
    def post_not_found_error_handler(request: Request, exc: PostNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)}
        )
