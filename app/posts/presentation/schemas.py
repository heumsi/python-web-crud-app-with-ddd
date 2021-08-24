from app.posts.domain.model import Post, PostBase


class CreatePostJsonRequest(PostBase):
    user_id: str
    user_password: str


class CreatePostJsonResponse(Post):
    pass


class UpdatePostJSONRequest(PostBase):
    pass


class UpdatePostJSONResponse(Post):
    pass
