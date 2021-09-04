from pydantic import BaseModel, Field
from ulid import ULID


class PostBase(BaseModel):
    title: str
    content: str
    user_id: str


class Post(PostBase):
    id: str = Field(default_factory=lambda: str(ULID()))

    class Config:
        arbitrary_types_allowed = True
