
from decimal import Decimal
from sqlalchemy import BigInteger, String, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.database import Base

from typing import Optional


class User(Base):
    __tablename__ = "user"
    
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, index=True)
    username: Mapped[str | None]
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    profile_photo: Mapped[str | None]
    
    wallet: Mapped[Optional["Wallet"]] = relationship(back_populates="user", lazy="joined", uselist=False, cascade="all, delete-orphan")
    

class Wallet(Base):
    __tablename__ = "wallet"
    
    balance: Mapped[Decimal] = mapped_column(Numeric(scale=2), default=Decimal("0.00"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), unique=True)
    
    user: Mapped["User"] = relationship(back_populates="wallet", lazy="joined")
    income_transactions: Mapped[list["IncomeTransaction"]] = relationship(back_populates="wallet", lazy="select")
    expense_transactions: Mapped[list["ExpenseTransaction"]] = relationship(back_populates="wallet", lazy="select")
    
    
class BaseTransaction(Base):
    __abstract__ = True
    
    value: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    comment: Mapped[str | None] = mapped_column(String(length=256))
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallet.id", ondelete="CASCADE"))
    
    
class IncomeTransaction(BaseTransaction):
    __tablename__ = "income_transaction"
    
    wallet: Mapped["Wallet"] = relationship(back_populates="income_transactions", lazy="joined")
    
class ExpenseTransaction(BaseTransaction):
    __tablename__ = "expense_transaction"
    
    wallet: Mapped["Wallet"] = relationship(back_populates="expense_transactions", lazy="joined")

