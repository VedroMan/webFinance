
# Валидация переменных через pydantic_settings
# https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage

import os

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    BASE_SITE: str | None = None
    BOT_TOKEN: str | None = None
    ADMIN_ID: str | None = None
    
    DB_URL: str = 'sqlite+aiosqlite:///./data/db.sqlite3'
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )
    
settings = Settings()
database_url = settings.DB_URL