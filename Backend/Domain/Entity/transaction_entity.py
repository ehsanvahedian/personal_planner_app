from dataclasses import dataclass, field
from datetime import datetime
from Domain.value_objects.Money import Money
from enum import Enum


class TransactionType(Enum):
    EXPENSE = "expense"
    INCOME = "income"

@dataclass
class transaction_entity:
    title: str
    amount: Money
    type: TransactionType
    source: str
    date: datetime
    description: str
    id: int | None = field(default=None)

    


