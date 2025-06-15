
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager
from asyncio import create_task

from loguru import logger

from aiogram import Bot, Dispatcher

from app.api.router import router as api_router
from app.views import router as view_router
from app.telegram_bot.router import router as user_router
from app.telegram_bot.handlers import router as bot_router
from app.config import settings

import uvicorn


async def setup_bot() -> tuple[Bot, Dispatcher, None]:
    bot = Bot(settings.BOT_TOKEN)
    dp = Dispatcher()
    log = logger.info("!Бот запущен!")
    
    dp.include_router(bot_router)
    
    await dp.start_polling(bot)
    
    return bot, dp, log


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("!Сервер запущен!")
    bot_task = create_task(setup_bot())
    yield
    bot_task.cancel()
    logger.info("!Сервер остановлен!")
    
    
def create_app() -> FastAPI:
    
    app = FastAPI(lifespan=lifespan)

    app.mount(
        "/static", 
        StaticFiles(directory="app/static"), 
        name="static"
    )
    
    origins = [
        "http://localhost:3000"
    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    register_routers(app)
    
    return app
    
def register_routers(app: FastAPI):
    
    app.include_router(api_router, tags=["wallet"])
    app.include_router(user_router, tags=["user"])
    app.include_router(view_router, tags=["views"])


app = create_app()


# MARK: -- Использовать только на время знакомства с проектом, лучше запускать через uvicorn
# Аналогичная команда через CLI: uvicorn app.main:app --host 0.0.0.0 --port 8008 --reload

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8008, reload=True)
    