from pydantic import BaseModel, Field
from datetime import datetime
from typing import Union
from Domain.value_objects.transaction_type import TransactionType
from Domain.value_objects.Money import Money


class transaction_pydantic_input(BaseModel):

    amount: int

    currency: str

    type: TransactionType

    title: Union[str | None] = None

    source: Union[str | None] = None

    date: datetime = Field(default=datetime.now())

    description: Union[str | None] = None

    def fix_amount(self):
        self.amount= Money(
            amount=self.amount,
            currency=self.currency
        )
        self.currency = None
        delattr(self, 'currency')


class transaction_pydantic(BaseModel):
    id: int

    amount: int

    currency: str

    type: TransactionType

    title: Union[str | None] = None

    source: Union[str | None] = None

    date: datetime = None

    description: Union[str | None] = None

    def fix_amount(self):
        self.amount= Money(
            amount=self.amount,
            currency=self.currency
        )
        self.currency = None
        delattr(self, 'currency')