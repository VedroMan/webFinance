
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.sessions import get_session_with_commit, get_session_without_commit

from app.api.schemas import (
    WalletModel,
    UserModel,
)

from app.api.dao import (
    UserDAO,
    WalletDAO,
    ExpenseTransactionDAO,
    IncomeTransactionDAO
)


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

# MARK: API

# User

@router.get("/api/wf/telegram-users/")
async def get_users(session: AsyncSession = Depends(get_session_without_commit)):
    return await UserDAO(session).read()

@router.get("/api/wf/telegram-user/{telegram_id}/")
async def get_user_by_tg_id(telegram_id: int, 
                            session: AsyncSession = Depends(get_session_without_commit)):
    return await UserDAO(session=session).get_user_by_telegram_id(telegram_id)

@router.post("/api/wf/telegram-user/")
async def create_telegram_user(values: UserModel,
                               session: AsyncSession = Depends(get_session_with_commit)):
    return await UserDAO(session).create(values)


# Wallet 

@router.get("/api/wf/wallets/")
async def get_wallets(session: AsyncSession = Depends(get_session_without_commit)):
    return await WalletDAO(session).read()

@router.get("/api/wf/wallet/{id}/")
async def get_wallet_by_id(id: int, session: AsyncSession = Depends(get_session_without_commit)):
    return await WalletDAO(session).find_one_or_none_by_id(data_id=id)

@router.get("/api/wf/wallet/{user_id}/")
async def get_wallet_by_user_id(user_id: int, 
                           session: AsyncSession = Depends(get_session_without_commit)):
    return await WalletDAO(session).get_wallet_by_user_id(user_id)

@router.get("/api/wf/wallet-transactions/{user_id}/")
async def get_wallet_with_transactions(user_id: int,
                                       session: AsyncSession = Depends(get_session_without_commit)):
    return await WalletDAO(session).get_wallet_with_transactions(user_id)

# Expense/Income transactions

@router.get("/api/wf/income-transactions/")
async def get_income_transactions(session: AsyncSession = Depends(get_session_without_commit)):
    return await IncomeTransactionDAO(session).read()

@router.get("/api/wf/income-transaction/{id}/")
async def get_income_transaction_by_id(id: int, 
                                       session: AsyncSession = Depends(get_session_without_commit)):
    return await IncomeTransactionDAO(session).find_one_or_none_by_id(data_id=id)

@router.get("/api/wf/expense-transactions/")
async def get_expense_transactions(session: AsyncSession = Depends(get_session_without_commit)):
    return await ExpenseTransactionDAO(session).read()

@router.get("/api/wf/expense-transaction/{id}/")
async def get_expense_transaction_by_id(id: int,
                                        session: AsyncSession = Depends(get_session_without_commit)):
    return await ExpenseTransactionDAO(session).find_one_or_none_by_id(data_id=id)


# MARK: Views

def template_response(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })

@router.get("/")
def home_view(request: Request):
    return template_response(request)
    
@router.get("/balance")
def balance_view(request: Request):
    return template_response(request)

@router.get("/budget")
def budget_view(request: Request):
    return template_response(request)

@router.get("/analytics")
def analytics_view(request: Request):
    return template_response(request)

@router.get("/settings")
def settings_view(request: Request):
    return template_response(request)