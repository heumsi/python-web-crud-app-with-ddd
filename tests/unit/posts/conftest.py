from typing import List

from app.modules.posts.domain.model import Post


def get_fake_post() -> Post:
    return Post(title="title1", content="content1", user_id="user1")


def get_fake_posts() -> List[Post]:
    return [
        Post(title="title1", content="content1", user_id="user1"),
        Post(title="title2", content="content2", user_id="user2"),
        Post(title="title3", content="content3", user_id="user3"),
    ]
