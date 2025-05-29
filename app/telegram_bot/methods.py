
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from asyncio import sleep

from app.config import settings
from app.api.schemas import UserBase
from app.telegram_bot.handlers import register_user

token = settings.BOT_TOKEN

bot = Bot(token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: Message) -> None:
    user_data = UserBase(
        telegram_id=message.from_user.id, # type: ignore
        first_name=message.from_user.first_name, # type: ignore
        username=message.from_user.username, # type: ignore
        last_name=message.from_user.last_name, # type: ignore
        profile_photo=None
    )
    
    user_data = await register_user(user_data)
    
    if "error" in user_data:
        er_message = await message.answer(
            f"Ошибка регистрации: { user_data['error'] }" 
        )
        return
    
    if user_data.get("message") == "Пользователь уже существует":
        name = message.from_user.first_name # type: ignore
        text_message = await message.answer(
            f"Вы уже зарегистрированы. С возвращением: { name }!"
        )
        
    else:
        await message.answer("Вы успешно зарегистрированы!!!")