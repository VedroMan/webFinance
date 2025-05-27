
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager
from asyncio import create_task

from loguru import logger

from app.api.router import router as api_router
from app.views import router as view_router
from app.telegram_bot.methods import dp, bot

import uvicorn

async def start_bot():
    logger.info("!Бот запущен!")
    await dp.start_polling(bot)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("!Сервер запущен!")
    bot_task = create_task(start_bot())
    yield
    bot_task.cancel()
    logger.info("!Сервер остановлен!")

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)
app.include_router(view_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


# MARK: -- Использовать только на время знакомства с проектом, лучше запускать через uvicorn
# Аналогичная команда через CLI: uvicorn app.main:app --host 0.0.0.0 --port 8008 --reload

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8008, reload=True)
    