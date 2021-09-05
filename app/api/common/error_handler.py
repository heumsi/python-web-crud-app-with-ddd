from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import JSONResponse

from app.modules.common.service_layer.exceptions import UnauthorizedError


def add_error_handler(app: FastAPI) -> None:
    @app.exception_handler(UnauthorizedError)
    def post_not_found_error_handler(request: Request, exc: UnauthorizedError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(exc)}
        )
