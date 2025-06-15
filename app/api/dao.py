
from app.api.schemas import TransactionBase
from app.dao.base import BaseDAO
from app.dao.models import (
    User, 
    Wallet, 
    IncomeTransaction, 
    ExpenseTransaction
)

from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from pydantic import BaseModel


class UserDAO(BaseDAO[User, BaseModel]):
    model = User
    
    async def get_user_by_telegram_id(self, telegram_id: int) -> User | None:
        query = select(self.model).filter_by(telegram_id=telegram_id)
        result = await self._session.execute(query)
        return result.scalar_one_or_none()


class WalletDAO(BaseDAO[Wallet, BaseModel]):
    model = Wallet
    
    async def get_wallet_by_user_id(self, user_id: int) -> Wallet | None:
        query = select(self.model).filter_by(user_id=user_id)
        result = await self._session.execute(query)
        return result.scalar_one_or_none()
    
    async def get_wallet_with_transactions(self, user_id: int) -> Wallet | None:
        query = (
            select(self.model)
            .filter_by(user_id=user_id)
            .options(joinedload(Wallet.income_transactions))
            .options(joinedload(Wallet.expense_transactions))
        )
        result = await self._session.execute(query)
        return result.scalar_one_or_none()
    
    
class IncomeTransactionDAO(BaseDAO[IncomeTransaction, TransactionBase]):
    model = IncomeTransaction
    
    async def create(self, values: TransactionBase) -> IncomeTransaction:
        wallet = await WalletDAO(self._session).find_one_or_none_by_id(values.wallet_id)
        if wallet is None:
            raise ValueError("Кошелёк отсутствует")
        
        transaction = await super().create(values)
        wallet.balance += transaction.value
        await self._session.flush()
        return transaction
    
    
class ExpenseTransactionDAO(BaseDAO[ExpenseTransaction, TransactionBase]):
    model = ExpenseTransaction
    
    async def create(self, values: TransactionBase) -> ExpenseTransaction:
        wallet = await WalletDAO(self._session).find_one_or_none_by_id(values.wallet_id)
        if wallet is None:
            raise ValueError("Кошелёк не найден")
        
        transaction = await super().create(values)
        wallet.balance -= transaction.value
        await self._session.flush()
        return transaction
        