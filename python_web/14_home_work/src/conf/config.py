from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    sqlalchemy_database_url: str= 'postgresql+asyncpg://postgres:567234@localhost:5432/rest_app'
    secret_key: str='secret_key'
    algorithm: str='HS256'
    mail_username: str = 'test_email'
    mail_password: str= 'test_password'
    mail_from: str= 'test_email'
    mail_port: int= 587
    mail_server: str= 'smtp.gmail.com'
    redis_host: str = 'localhost'
    redis_port: int = 6379
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    cloudinary_name: str= 'test_cloudinary_name'
    cloudinary_api_key: str= 'test_cloudinary_api_key'
    cloudinary_api_secret: str= 'test_cloudinary_api_secret'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


settings = Settings()
