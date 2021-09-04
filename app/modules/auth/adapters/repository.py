from dataset import Database, Table

from app.modules.auth.domain.model import User
from app.modules.auth.domain.repository import AuthRepository


class DatasetAuthRepository(AuthRepository):
    table_name = "user"

    def __init__(self, db: Database) -> None:
        self._db = db

    def find_by_user_id(self, user_id: str) -> User:
        table: Table = self._db.get_table(self.table_name)
        user_dict = table.find_one(id=user_id)
        if user_dict:
            return User(id=user_dict["id"], password=user_dict["password"])
