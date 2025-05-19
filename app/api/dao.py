
from app.dao.base import BaseDAO
from app.dao.models import (
    User, 
    Wallet, 
    IncomeTransaction, 
    ExpenseTransaction
)

from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

class UserDAO(BaseDAO[User]):
    model = User
    
    async def get_user_by_telegram_id(self, telegram_id: int) -> User | None:
        query = select(self.model).filter_by(telegram_id=telegram_id)
        result = await self._session.execute(query)
        return result.scalar_one_or_none()


class WalletDAO(BaseDAO[Wallet]):
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
    
    
class IncomeTransactionDAO(BaseDAO[IncomeTransaction]):
    model = IncomeTransaction
    
class ExpenseTransactionDao(BaseDAO[ExpenseTransaction]):
    model = ExpenseTransaction