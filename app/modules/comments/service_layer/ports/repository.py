from abc import ABC, abstractmethod
from typing import List, Optional

from app.modules.comments.domain.model import Comment


class CommentRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Comment]:
        pass

    @abstractmethod
    def find_by_id(self, comment_id: str) -> Optional[Comment]:
        pass

    @abstractmethod
    def find_all_by_user_id(self, user_id: str) -> List[Comment]:
        pass

    @abstractmethod
    def find_all_by_post_id(self, post_id: str) -> List[Comment]:
        pass

    @abstractmethod
    def save(self, comment: Comment) -> Comment:
        pass

    @abstractmethod
    def delete_by_id(self, comment_id: str) -> Optional[Comment]:
        pass
