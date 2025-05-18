
from app.dao.base import BaseDAO
from app.dao.models import User, Wallet, IncomeTransaction, ExpenseTransaction

class UserDAO(BaseDAO):
    model = User

class WalletDAO(BaseDAO):
    model = Wallet
    
class IncomeTransactionDAO(BaseDAO):
    model = IncomeTransaction
    
class ExpenseTransactionDao(BaseDAO):
    model = ExpenseTransaction