from abc import ABC, abstractmethod
from typing import List, Optional

from app.modules.posts.domain.model import Post


class PostRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Post]:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Post]:
        pass

    @abstractmethod
    def find_by_user_id(self, user_id: str) -> List[Post]:
        pass

    @abstractmethod
    def save(self, post: Post) -> Post:
        pass

    @abstractmethod
    def delete_by_id(self, id: str) -> Optional[Post]:
        pass

    @abstractmethod
    def delete_all_by_user_id(self, user_id: str) -> None:
        pass
