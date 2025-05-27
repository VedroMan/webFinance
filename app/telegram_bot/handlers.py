
from httpx import (
    AsyncClient,
    HTTPStatusError,
    RequestError
)

from app.api.schemas import UserData
from app.config import settings


site = settings.BASE_SITE

async def register_user(user: UserData):
    
    url = f"{site}/api/wf/telegram-user/"
    payload = {
        "telegram_id": user.telegram_id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "profile_photo": user.profile_photo or ""
    }
    
    async with AsyncClient() as client:
        try:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as e:
            return { "error" : f"Ошибка {e.response.status_code}: {e.response.text} "}
        except RequestError as e:
            return { "error" : f"Сбой подключения к API: {str(e)}" }
        