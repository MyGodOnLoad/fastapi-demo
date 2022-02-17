
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str
    TITLE: str
    DESCRIPTION: str
    VERSION: str

    CELERY_NAME: str
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_SERVER: str
    RABBITMQ_PORT: str

    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_SERVER: str
    MYSQL_DB: str


settings = Settings()
