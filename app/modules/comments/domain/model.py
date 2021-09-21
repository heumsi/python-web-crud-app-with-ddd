from pydantic import BaseModel, Field
from ulid import ULID


class Comment(BaseModel):
    id: str = Field(default_factory=lambda: str(ULID()))
    user_id: str
    post_id: str
    content: str

    class Config:
        arbitrary_types_allowed = True
