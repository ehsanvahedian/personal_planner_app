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

class transaction_ORM(Base):
    __tablename__ = "document"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    amount: Mapped[Money]
    type: Mapped[TransactionType]
    source: Mapped[str]
    date: Mapped[datetime]
    description: Mapped[str]

