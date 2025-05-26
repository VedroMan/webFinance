
from pydantic import (
    BaseModel, 
    ConfigDict, 
    Field
)

from decimal import Decimal
from typing import Optional

class UserModel(BaseModel):
    id: int
    wallet: Optional["WalletModel"] = None
    
    model_config = ConfigDict(from_attributes=True)
    
class UserData(UserModel):
    telegram_id: int
    username: str | None = None
    first_name: str
    last_name: str | None = None
    profile_photo: str
    
class WalletModel(BaseModel):
    id: int
    user: "UserModel"
    income_transactions: list["TransactionData"] = Field(default_factory=list)
    expense_transactions: list["TransactionData"] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)
    
class WalletData(WalletModel):
    balance: Decimal = Field(decimal_places=2, default=Decimal("0.00"))
    user_id: int


class TransactionModel(BaseModel):
    id: int
    
    wallet: "WalletModel"
    model_config = ConfigDict(from_attributes=True)
    
class TransactionData(TransactionModel):
    value: Decimal = Field(max_digits=10, decimal_places=2)
    comment: str = Field(max_length=256)
    wallet_id: int
    
    

UserModel.model_rebuild()
WalletModel.model_rebuild()
TransactionModel.model_rebuild()