from pydantic import BaseModel


class CreatePostJsonRequest(BaseModel):
    title: str
    content: str


class CreatePostJsonResponse(BaseModel):
    id: str
    title: str
    content: str
    user_id: str


class UpdatePostJSONRequest(BaseModel):
    title: str
    content: str


class UpdatePostJSONResponse(BaseModel):
    id: str
    title: str
    content: str
    user_id: str
