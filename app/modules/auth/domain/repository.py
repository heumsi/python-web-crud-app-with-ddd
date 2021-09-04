from abc import ABC, abstractmethod

from app.modules.auth.domain.model import User


class AuthRepository(ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> User:
        pass
