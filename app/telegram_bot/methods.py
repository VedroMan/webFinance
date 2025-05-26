
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from asyncio import sleep

from app.config import settings

token = settings.BOT_TOKEN

bot = Bot(token)
dp = Dispatcher()

@dp.message(Command("start"))
async def greeting(message: Message) -> None:
    await message.answer("Привет!!!")
