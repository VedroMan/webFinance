
# Валидация переменных через pydantic_settings
# https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage

import os

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    BASE_SITE: str 
    BOT_TOKEN: str
    ADMIN_ID: str
    
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    
    @property
    def DB_URL(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )
    
settings = Settings() # type: ignore
database_url = settings.DB_URL