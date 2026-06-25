from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Union

class money_pydantic(BaseModel):
    amount: int
    currency: str

    
class TransactionType(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"


class transaction_pydantic(BaseModel):
    title: str

    amount: money_pydantic

    type: TransactionType

    source: Union[str | None] = None

    date: datetime = Field(
        default_factory=datetime.now
    )

    description: Union[str | None] = None