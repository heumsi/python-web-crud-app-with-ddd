from fastapi import APIRouter
from starlette import status

from app.api.comments.entrypoints.create_comment import create_comment
from app.api.comments.entrypoints.delete_comment import delete_comment

router = APIRouter()
router.add_api_route(
    path="/",
    endpoint=create_comment,
    methods=["POST"],
    status_code=status.HTTP_201_CREATED,
)
router.add_api_route(
    path="/{comment_id}",
    endpoint=delete_comment,
    methods=["DELETE"],
    status_code=status.HTTP_204_NO_CONTENT,
)
