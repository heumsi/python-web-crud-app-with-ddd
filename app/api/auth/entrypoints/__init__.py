from fastapi import APIRouter
from starlette import status

from app.api.auth.entrypoints.get_token import get_token
from app.api.auth.entrypoints.get_token_payload import (
    get_token_payload,
)

router = APIRouter()
router.add_api_route(
    path="/token", endpoint=get_token, methods=["POST"], status_code=status.HTTP_200_OK
)
router.add_api_route(
    path="/token",
    endpoint=get_token_payload,
    methods=["GET"],
    status_code=status.HTTP_200_OK,
)
