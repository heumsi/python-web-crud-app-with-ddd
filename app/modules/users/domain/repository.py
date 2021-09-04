from abc import ABC, abstractmethod
from typing import List, Optional

from app.modules.users.domain.model import User


class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_by_id(self, id: str) -> Optional[User]:
        pass
