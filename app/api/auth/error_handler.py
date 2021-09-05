from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.modules.auth.service_layer.exceptions import (
    TokenCreateError,
    UserNotFoundError, PasswordInvalidError, TokenInvalidError,
)


def add_error_handler(app: FastAPI) -> None:
    # applicaiton layer error
    @app.exception_handler(UserNotFoundError)
    def user_found_error_handler(request: Request, exc: UserNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)}
        )

    @app.exception_handler(TokenCreateError)
    def token_create_error_handler(request: Request, exc: TokenCreateError):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(exc)},
        )

    @app.exception_handler(PasswordInvalidError)
    def password_invalid_error_handler(request: Request, exc: PasswordInvalidError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(exc)},
        )

    @app.exception_handler(TokenInvalidError)
    def password_invalid_error_handler(request: Request, exc: TokenInvalidError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(exc)},
        )
