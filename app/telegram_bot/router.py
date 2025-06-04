
# Telegram-user router

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.sessions import get_session_with_commit, get_session_without_commit
from app.api.schemas import UserBase
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

@router.post("/telegram-user/")
async def create_telegram_user(
    values: UserBase, 
    session: AsyncSession = Depends(get_session_with_commit)
):
    if await UserDAO(session).get_user_by_telegram_id(telegram_id=values.telegram_id):
        return { "status" : "exists" }
    
    user = await UserDAO(session).create(values)
    return { "status" : "created", "user" : user }
