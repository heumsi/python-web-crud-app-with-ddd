from dataset import Database
from dataset.types import Types


def create_tables(db: Database) -> None:
    db.create_table("user", primary_id="id", primary_type=Types.string)
    db.create_table("post", primary_id="id", primary_type=Types.string)
