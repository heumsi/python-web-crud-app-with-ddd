from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.modules.comments.service_layer.exceptions import CommentNotFoundError


def add_error_handler(app: FastAPI) -> None:
    # applicaiton layer error
    @app.exception_handler(CommentNotFoundError)
    def user_found_error_handler(request: Request, exc: CommentNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)}
        )
