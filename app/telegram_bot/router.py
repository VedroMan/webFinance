
# Telegram-user router

from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.sessions import get_session_with_commit, get_session_without_commit
from app.api.schemas import UserBase, UserModel
from app.api.dao import UserDAO

router = APIRouter()

@router.get("/api/wf/telegram-users/")
async def get_users(session: AsyncSession = Depends(get_session_without_commit)):
    return await UserDAO(session).read()

@router.get("/api/wf/telegram-user/{telegram_id}/")
async def get_user_by_tg_id(
    telegram_id: int, 
    session: AsyncSession = Depends(get_session_without_commit)
):
    return await UserDAO(session).get_user_by_telegram_id(telegram_id)

@router.post(
    "/telegram-user/",
    status_code=status.HTTP_201_CREATED
)
async def create_telegram_user(
    user_data: UserBase, 
    session: AsyncSession = Depends(get_session_with_commit)
) -> dict:
    if await UserDAO(session).get_user_by_telegram_id(telegram_id=user_data.telegram_id):
        return { "status" : "exists" }
    
    user = await UserDAO(session).create(user_data)
    return { 
            "status" : "created", 
            "user" : UserBase.model_validate(user, from_attributes=True)
        }
