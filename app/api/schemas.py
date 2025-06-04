
from pydantic import (
    BaseModel, 
    ConfigDict, 
    Field
)

from decimal import Decimal
from typing import Optional


class UserBase(BaseModel):
    telegram_id: int
    username: str | None = None
    first_name: str
    last_name: str | None = None
    profile_photo: str = Field(default="")

class UserModel(UserBase):
    id: int
    wallet: Optional["WalletModel"] = None
    
    model_config = ConfigDict(from_attributes=True)
    
    
class WalletBase(BaseModel):
    balance: Decimal = Field(decimal_places=2, default=Decimal("0.00"))
    user_id: int

class WalletModel(WalletBase):
    id: int
    user: "UserModel"
    income_transactions: list["TransactionModel"] = Field(default_factory=list)
    expense_transactions: list["TransactionModel"] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)


class TransactionBase(BaseModel):
    value: Decimal = Field(max_digits=10, decimal_places=2)
    comment: str = Field(max_length=256)
    wallet_id: int
    
class TransactionModel(TransactionBase):
    id: int
    wallet: "WalletModel"
    
    model_config = ConfigDict(from_attributes=True)
    

UserModel.model_rebuild()
WalletModel.model_rebuild()
TransactionModel.model_rebuild()