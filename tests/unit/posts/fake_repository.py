from typing import List, Optional

from app.modules.posts.domain.model import Post
from app.modules.posts.domain.repository import PostRepository


class FakePostRepository(PostRepository):


    def __init__(self, posts: Optional[List[Post]] = None) -> None:
        if not posts:
            self.posts = {}
        else:
            self.posts = {str(post.id): post for post in posts}

    def find_by_id(self, id: str) -> Optional[Post]:
        return self.posts.get(id, None)

    def find_by_user_id(self, user_id: str) -> List[Post]:
        return [post for id, post in self.posts.items() if post.user_id == user_id]

    def find_all(self) -> List[Post]:
        return list(self.posts.values())

    def save(self, post: Post) -> Post:
        self.posts[str(post.id)] = post
        return post

    def delete_by_id(self, id: str) -> Optional[Post]:
        return self.posts.pop(id, None)

    def delete_all_by_user_id(self, user_id: str) -> None:
        for id, post in self.posts.items():
            if post['user_id'] == user_id:
                del self.posts[id]
    