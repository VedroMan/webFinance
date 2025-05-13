
from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger

from app.api.router import router as router_api

import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("!Сервер запущен!")
    yield
    logger.info("!Сервер остановлен!")

app = FastAPI(lifespan=lifespan)

app.include_router(router=router_api)


# MARK: -- Использовать только на время знакомства с проектом, лучше запускать через uvicorn
# Аналогичная команда через CLI: uvicorn app.main:app --host 0.0.0.0 --port 8008 --reload

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8008, reload=True)
    