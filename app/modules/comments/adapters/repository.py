from typing import List, Optional

from dataset import Database

from app.modules.comments.domain.model import Comment
from app.modules.comments.service_layer.ports.repository import CommentRepository
from app.modules.common.adapters.repository import DatasetRepository


class DatasetCommentRepository(CommentRepository, DatasetRepository):
    def __init__(self, db: Database) -> None:
        super().__init__(db=db)

    def find_all(self) -> List[Comment]:
        table = self.get_table()
        return [Comment(**dict_) for dict_ in table.all()]

    def find_by_id(self, comment_id: str) -> Optional[Comment]:
        table = self.get_table()
        dict_ = table.find_one(id=comment_id)
        if dict_:
            return Comment(**dict_)

    def find_all_by_user_id(self, user_id: str) -> List[Comment]:
        table = self.get_table()
        return [Comment(**dict_) for dict_ in table.find(user_id=user_id)]

    def find_all_by_post_id(self, post_id: str) -> List[Comment]:
        table = self.get_table()
        return [Comment(**dict_) for dict_ in table.find(user_id=post_id)]

    def save(self, comment: Comment) -> Comment:
        table = self.get_table()
        table.upsert(comment.dict(), keys=["id"])
        return comment

    def delete_by_id(self, comment_id: str) -> Optional[Comment]:
        table = self.get_table()
        dict_ = table.find_one(id=comment_id)
        table.delete(id=comment_id)
        if dict_:
            return Comment(**dict_)

    @property
    def table_name(self) -> str:
        return "comment"
