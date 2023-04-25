import secrets
from os import environ
from pydantic import BaseSettings

def get_url() ->str:
    server = environ.get("POSTGRES_SERVER")
    username = environ.get("POSTGRES_USER")
    password = environ.get("POSTGRES_PASSWORD")
    database = environ.get("POSTGRES_DB")

    return f"postgresql://{username}:{password}@{server}/{database}"

class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    ALGORITHM = "HS256"

    SQLALCHEMY_DATABASE_URL: str = get_url()


settings = Settings()