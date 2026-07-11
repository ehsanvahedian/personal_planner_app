from pydantic import BaseModel, Field
from datetime import datetime
from typing import Union
from Domain.value_objects.transaction_type import TransactionType

class transaction_pydantic_input(BaseModel):

    amount: int

    type: TransactionType

    title: Union[str | None] = None

    source: Union[str | None] = None

    date: datetime = Field(default=datetime.now())

    description: Union[str | None] = None


class transaction_pydantic(BaseModel):
    id: int

    amount: int

    type: Union[TransactionType | None] = None

    title: Union[str | None] = None

    source: Union[str | None] = None

    date: Union[datetime | None] = None

    description: Union[str | None] = None
