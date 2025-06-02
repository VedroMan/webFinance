
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from app.api.schemas import UserBase
from app.telegram_bot.methods import register_user

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    user_data = UserBase(
        telegram_id=message.from_user.id, # type: ignore
        first_name=message.from_user.first_name, # type: ignore
        username=message.from_user.username, # type: ignore
        last_name=message.from_user.last_name, # type: ignore
        profile_photo=None
    )
    
    user_data = await register_user(user_data)
    
    if "error" in user_data:
        await message.answer(
            f"Ошибка регистрации: { user_data['error'] }" 
        )
        return
    
    if user_data.get("message") == "Пользователь уже существует":
        name = message.from_user.first_name # type: ignore
        await message.answer(
            f"Вы уже зарегистрированы. С возвращением: { name }!"
        )
        
    else:
        await message.answer("Вы успешно зарегистрированы!!!")
    
@router.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer("Проверочкаааааа")
