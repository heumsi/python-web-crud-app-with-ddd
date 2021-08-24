from fastapi import status, FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.common.domain.exceptions import AuthroizeError


def add_common_error_handler(app: FastAPI) -> None:
    # @app.exception_handler(UserNotFoundError)
    # def user_not_found_error_handler(request: Request, exc: UserNotFoundError):
    #     return JSONResponse(
    #         status_code=status.HTTP_404_NOT_FOUND, content={"message": str(exc)}
    #     )

    @app.exception_handler(AuthroizeError)
    def authorize_user_error_handler(request: Request, exc: AuthroizeError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"message": str(exc)}
        )

    # @app.exception_handler(PostNotFoundError)
    # def post_not_found_error_handler(request: Request, exc: PostNotFoundError):
    #     return JSONResponse(
    #         status_code=status.HTTP_404_NOT_FOUND, content={"message": str(exc)}
    #     )

