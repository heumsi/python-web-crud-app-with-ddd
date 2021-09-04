from pydantic import BaseSettings, Field


class Config(BaseSettings):
    jwt_secret_key: str = Field(env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(env="JWT_ALGORITHM")
