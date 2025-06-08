
from httpx import (
    AsyncClient,
    HTTPStatusError,
    RequestError
)

from app.api.schemas import UserBase
from app.config import settings

from aiogram import Bot

base_url = settings.BASE_SITE

async def register_user(user: UserBase):
    
    url = "/telegram-user/"
    data = user.model_dump()
    
    async with AsyncClient(base_url=base_url) as client:
        try:
            response = await client.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as e:
            return {
                "status" : "error",
                "error" : f"Ошибка {e.response.status_code}: {e.response.text}"
            }
        except RequestError as e:
            return {
                "status" : "error",
                "error" : f"Сбой подключения: {str(e)}"
            }
        
async def get_user_photo_url(bot: Bot, user_id: int) -> str | None:
    result = await bot.get_user_profile_photos(user_id)
    if not result.photos:
        return None
    
    photo = result.photos[0][-1]
    file = await bot.get_file(photo.file_id)
    
    return f"https://api.telegram.org/file/bot{bot.token}/{file.file_path}"
    
        