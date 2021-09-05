from pydantic import BaseSettings, Field


class AuthConfig(BaseSettings):
    jwt_secret_key: str = Field(env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(env="JWT_ALGORITHM")
