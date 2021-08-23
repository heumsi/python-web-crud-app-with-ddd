from typing import List, Optional

from dataset import Database, Table
from dataset.types import Types

from app.posts.domain.model import Post
from app.posts.domain.repository import PostRepository


class DatasetPostRepository(PostRepository):
    table_name = "post"

    def __init__(self, db: Database) -> None:
        self._db = db

    def find_by_id(self, id: str) -> Optional[Post]:
        table: Table = self._db.get_table(self.table_name)
        post_dict = table.find_one(id=id)
        if post_dict:
            return Post(**post_dict)

    def find_by_user_id(self, user_id: str) -> List[Post]:
        table: Table = self._db.get_table(self.table_name)
        return [Post(**post_dict) for post_dict in table.find(user_id=user_id)]

    def find_all(self) -> List[Post]:
        table: Table = self._db.get_table(self.table_name)
        return [Post(**post_dict) for post_dict in table.all()]

    def save(self, post: Post) -> Post:
        table: Table = self._db.get_table(self.table_name)
        return table.upsert(post.dict(), keys=["id"])

    def delete_by_id(self, id: str) -> Optional[Post]:
        table: Table = self._db.get_table(self.table_name)
        return table.delete(id=id)


def create_tables(db: Database) -> None:
    db.create_table("post", primary_id="id", primary_type=Types.string)
