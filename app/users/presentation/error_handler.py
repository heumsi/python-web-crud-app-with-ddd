from fastapi import status, FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.users.domain.exceptions import UserNotFoundError


def add_error_handler(app: FastAPI) -> None:
    @app.exception_handler(UserNotFoundError)
    def user_not_found_error_handler(request: Request, exc: UserNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": str(exc)}
        )
