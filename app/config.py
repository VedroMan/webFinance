
# Валидация переменных через pydantic_settings
# https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage

import os

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    BASE_SITE: str
    BOT_TOKEN: str
    ADMIN_ID: str
    
    DB_URL: str = 'sqlite+aiosqlite:///./data/db.sqlite3'
    
    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )
    
settings = Settings()
database_url = settings.DB_URL