
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from app.api.schemas import UserBase
from app.telegram_bot.methods import register_user

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    user = message.from_user
    if not user:
        await message.answer("Не удалось получить информацию о пользователе")
        return
    
    user_data = UserBase(
        telegram_id=user.id,
        first_name=user.first_name,
        username=user.username,
        last_name=user.last_name,
        profile_photo=""
    )
    
    result = await register_user(user_data)
    
    if result["status"] == "exists":
        await message.answer(f"С возвращением, { user.first_name }!")
    elif result["status"] == "created":
        await message.answer("🎉 Регистрация успешна!")
    else:
        err_msg = result.get("message", "Неизвестная ошибка")
        await message.answer(f"⚠️ Ошибка: {result['err_msg']}")
        
    
@router.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer("Проверочкаааааа")
