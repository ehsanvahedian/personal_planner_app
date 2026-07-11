from .Base import Base
from dataclasses import dataclass
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from Domain.Entity.transaction_entity import transaction_entity
from Domain.value_objects.transaction_type import TransactionType


class transaction_ORM(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=True)
    amount: Mapped[int]
    type: Mapped[TransactionType]
    source: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[datetime]
    description: Mapped[str] = mapped_column(nullable=True)

    def to_entity(self) -> transaction_entity:
        return transaction_entity(
            title=self.title,
            amount=self.amount,
            type=self.type,
            source=self.source,
            date=self.date,
            description=self.description,
            id=self.id
        )
    
@dataclass 
class transactions_list:
    status: str
    transactions: list[transaction_entity] = None
    message: str = None