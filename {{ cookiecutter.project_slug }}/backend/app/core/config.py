import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    ALGORITHM = "HS256"

    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sql_app.db"


settings = Settings()