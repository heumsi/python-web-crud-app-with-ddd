from pydantic import BaseModel, Field
from ulid import ULID


class PostBase(BaseModel):
    title: str
    content: str
    user_id: str


# def create_ulid_as_string():
#     return str(ULID())


class Post(PostBase):
    id: str = Field(default_factory=lambda: str(ULID()))

    class Config:
        arbitrary_types_allowed = True
