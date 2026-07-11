from dataclasses import dataclass, field, replace
from datetime import datetime

from enum import Enum


class TransactionType(Enum):
    EXPENSE = "expense"
    INCOME = "income"

@dataclass
class transaction_entity:
    title: str
    amount: int
    type: TransactionType
    source: str
    date: datetime
    description: str
    id: int | None = field(default=None)

    def replace_items(self, updated_data):
        return replace(self, **updated_data)


