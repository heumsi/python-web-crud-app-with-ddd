from typing import List, Optional

from app.users.domain.model import User
from app.users.domain.repository import UserRepository


class FakeUserRepository(UserRepository):
    def __init__(self, users: Optional[List[User]] = None) -> None:
        if not users:
            self.users = []
        else:
            self.users = users

    def find_by_id(self, id: str) -> Optional[User]:
        return next((user for user in self.users if user.id == id), None)

    def find_all(self) -> List[User]:
        return self.users

    def save(self, user: User) -> User:
        self.users.append(user)
        return user

    def delete_by_id(self, id: str) -> Optional[User]:
        for index, user in enumerate(self.users):
            if user.id == id:
                self.users.pop(index)
                return user
        return None
