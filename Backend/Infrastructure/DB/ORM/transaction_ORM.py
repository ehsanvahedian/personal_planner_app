from sqlalchemy import TypeDecorator, JSON
from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from enum import Enum
from Domain.value_objects.Money import Money
from Domain.value_objects.transaction_type import TransactionType


class MoneyType(TypeDecorator):
    impl = JSON
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None

        return {
            "amount": value.amount,
            "currency": value.currency
        }

    def process_result_value(self, value, dialect):
        if value is None:
            return None

        return Money(
            amount=value["amount"],
            currency=value["currency"]
        )

class transaction_ORM(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=True)
    amount: Mapped[Money] = mapped_column(MoneyType())
    type: Mapped[TransactionType]
    source: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[datetime]
    description: Mapped[str] = mapped_column(nullable=True)

