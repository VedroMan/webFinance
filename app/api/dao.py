
from app.dao.base import BaseDAO
from app.dao.models import User, Transaction

class UserDAO(BaseDAO):
    model = User
    
class TransactionDAO(BaseDAO):
    model = Transaction