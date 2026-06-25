from sqlalchemy import TypeDecorator, JSON
from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    EXPENSE = "expense"
    INCOME = "income"

class Money:
    amount: int
    currency: str

    def __dict__(self):
        return {"amount": self.amount, "currency": self.currency}



class transaction_ORM(Base):
    __tablename__ = "transactions"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    amount: Mapped[dict] = mapped_column(JSON)
    type: Mapped[TransactionType]
    source: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[datetime]
    description: Mapped[str] = mapped_column(nullable=True)

