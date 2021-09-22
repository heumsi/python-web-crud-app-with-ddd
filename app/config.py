from pydantic import BaseSettings

from app.infrastructures.persistence import DBConfig
from app.modules.auth.config import AuthConfig


class AppConfig(BaseSettings):
    # db_url: str = Field(Required, env="DB_URL", default="sqlite:///sqlite.db")
    db: DBConfig = DBConfig()
    auth: AuthConfig = AuthConfig()
