
from pydantic import (
    BaseModel, 
    ConfigDict, 
    Field
)

from decimal import Decimal
from typing import Optional

class UserModel(BaseModel):
    id: int
    telegram_id: int
    username: str | None = None
    first_name: str
    last_name: str | None = None
    profile_photo: str
    
    wallet: Optional["WalletModel"] = None
    
    model_config = ConfigDict(from_attributes=True)
    
    
class WalletModel(BaseModel):
    id: int
    balance: Decimal = Field(decimal_places=2, default=Decimal("0.00"))
    user_id: int
    
    user: "UserModel"
    income_transactions: list["IncomeTransactionModel"] = Field(default_factory=list)
    expense_transactions: list["ExpenseTransactionModel"] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)
    
    
class TransactionModel(BaseModel):
    id: int
    value: Decimal = Field(max_digits=10, decimal_places=2)
    comment: str = Field(max_length=256)
    wallet_id: int
    
    model_config = ConfigDict(from_attributes=True)
    
    
class IncomeTransactionModel(TransactionModel):
    wallet: "WalletModel"
    model_config = ConfigDict(from_attributes=True)
    
    
class ExpenseTransactionModel(TransactionModel):
    wallet: "WalletModel"
    model_config = ConfigDict(from_attributes=True)

    
UserModel.model_rebuild()
WalletModel.model_rebuild()
IncomeTransactionModel.model_rebuild()
ExpenseTransactionModel.model_rebuild()