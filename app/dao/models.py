
from typing import List
from decimal import Decimal
from sqlalchemy import Integer, Text, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.database import Base


class User(Base):
    __tablename__="user"
    
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False, index=True)
    username: Mapped[str | None]
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    profile_photo: Mapped[str]
    
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="user", lazy="select", cascade="all")
    
    
class Transaction(Base):
    __tablename__="transaction"
    
    value: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    comment: Mapped[str] = mapped_column(Text(length=256))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    
    user: Mapped["User"] = relationship(back_populates="transactions", lazy="select")
    
    