
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.sessions import get_session_with_commit, get_session_without_commit

from app.api.schemas import (
    WalletBase,
    WalletModel,
    TransactionBase,
    TransactionModel,
)

from app.api.dao import (
    WalletDAO,
    ExpenseTransactionDAO,
    IncomeTransactionDAO
)


router = APIRouter()


# Wallet 

@router.get("/api/wf/wallets/")
async def get_wallets(session: AsyncSession = Depends(get_session_without_commit)):
    return await WalletDAO(session).read()

@router.get("/api/wf/wallet/{wallet_id}/")
async def get_wallet_by_id(
    wallet_id: int, 
    session: AsyncSession = Depends(get_session_without_commit)
):
    return await WalletDAO(session).find_one_or_none_by_id(data_id=wallet_id)

@router.get("/api/wf/wallet/{user_id}/")
async def get_wallet_by_user_id(
    user_id: int, 
    session: AsyncSession = Depends(get_session_without_commit)
):
    return await WalletDAO(session).get_wallet_by_user_id(user_id)

@router.get("/api/wf/wallet-transactions/{user_id}/")
async def get_wallet_with_transactions(
    user_id: int,
    session: AsyncSession = Depends(get_session_without_commit)
):
    return await WalletDAO(session).get_wallet_with_transactions(user_id)

@router.post(
    "/wallet/", 
    response_model=WalletModel, 
    status_code=status.HTTP_201_CREATED
)
async def create_wallet(
    wallet_data: WalletBase,
    session: AsyncSession = Depends(get_session_with_commit)
) -> WalletModel:
    
    if await WalletDAO(session).get_wallet_by_user_id(user_id=wallet_data.user_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Такой кошелёк уже существует"
        )
        
    wallet = await WalletDAO(session).create(wallet_data)
    return WalletModel.model_validate(wallet)
    
# Expense/Income transactions

@router.get("/api/wf/income-transactions/")
async def get_income_transactions(session: AsyncSession = Depends(get_session_without_commit)):
    return await IncomeTransactionDAO(session).read()

@router.get("/api/wf/income-transaction/{id}/")
async def get_income_transaction_by_id(
    id: int, 
    session: AsyncSession = Depends(get_session_without_commit)
):
    return await IncomeTransactionDAO(session).find_one_or_none_by_id(id)

@router.post("/income-transaction/")
async def create_income_transaction(
    data: TransactionBase,
    session: AsyncSession = Depends(get_session_with_commit)
) -> TransactionModel:
    transaction = await IncomeTransactionDAO(session).create(data)
    return TransactionModel.model_validate(transaction)


@router.get("/api/wf/expense-transactions/")
async def get_expense_transactions(session: AsyncSession = Depends(get_session_without_commit)):
    return await ExpenseTransactionDAO(session).read()

@router.get("/api/wf/expense-transaction/{id}/")
async def get_expense_transaction_by_id(
    id: int,
    session: AsyncSession = Depends(get_session_without_commit)
):
    return await ExpenseTransactionDAO(session).find_one_or_none_by_id(id)

@router.post("/expense-transaction/")
async def create_expense_transaction(
    data: TransactionBase,
    session: AsyncSession = Depends(get_session_with_commit)
) -> TransactionModel:
    transaction = await ExpenseTransactionDAO(session).create(data)
    return TransactionModel.model_validate(transaction)
