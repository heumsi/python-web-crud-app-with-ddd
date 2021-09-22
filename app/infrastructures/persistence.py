from dataset import Database
from dataset.types import Types
from pydantic import BaseSettings, Field, Required


def create_tables(db: Database) -> None:
    db.create_table("user", primary_id="id", primary_type=Types.string)
    db.create_table("post", primary_id="id", primary_type=Types.string)
    db.create_table("comment", primary_id="id", primary_type=Types.string)


class DBConfig(BaseSettings):
    url: str = Field(Required, env="DB_URL")
