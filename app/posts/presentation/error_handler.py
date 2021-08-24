from fastapi import status, FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.posts.domain.exceptions import PostNotFoundError


def add_error_handler(app: FastAPI) -> None:
    @app.exception_handler(PostNotFoundError)
    def post_not_found_error_handler(request: Request, exc: PostNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": str(exc)}
        )
