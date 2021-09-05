from typing import List, Optional

from dataset import Database, Table

from app.modules.users.domain.model import User
from app.modules.users.domain.repository import UserRepository


class DatasetUserRepository(UserRepository):
    table_name = "user"

    def __init__(self, db: Database) -> None:
        self._db = db

    def find_by_id(self, id: str) -> Optional[User]:
        table: Table = self._db.get_table(self.table_name)
        user_dict = table.find_one(id=id)
        if user_dict:
            return User(**user_dict)

    def find_all(self) -> List[User]:
        table: Table = self._db.get_table(self.table_name)
        return [User(**user_dict) for user_dict in table.all()]

    def save(self, user: User) -> User:
        table: Table = self._db.get_table(self.table_name)
        table.upsert(user.dict(), keys=["id"])
        return user

    def delete_by_id(self, id: str) -> Optional[User]:
        table: Table = self._db.get_table(self.table_name)
        user_dict = table.find_one(id=id)
        if user_dict:
            table.delete(id=id)
            return User(**user_dict)

