
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from app.api.schemas import TransactionModel, UserModel

router = APIRouter()

@router.get("/")
async def home_page():
    return "Server started!!!"
