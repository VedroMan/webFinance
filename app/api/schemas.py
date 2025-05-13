
from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal

class TelegramIDModel(BaseModel):
    telegram_id: int
    model_config = ConfigDict(from_attributes=True)
    
class UserModel(TelegramIDModel):
    id: int
    username: str | None
    first_name: str
    last_name: str | None
    profile_photo: str
    transactions: list["TransactionModel"] = Field(exclude=True)
    model_config = ConfigDict(from_attributes=True)
    
class TransactionModel(BaseModel):
    id: int
    value: Decimal = Field(max_digits=10, decimal_places=2)
    comment: str = Field(max_length=256)
    user_id: int
    model_config = ConfigDict(from_attributes=True)
    
UserModel.model_rebuild()
TransactionModel.model_rebuild()