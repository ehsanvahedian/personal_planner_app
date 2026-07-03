import click
from ..API.pydantic_models.transaction_pydantic import transaction_pydantic

# class transaction_pydantic(BaseModel):
#     title: str

#     amount: money_pydantic

#     type: TransactionType

#     source: Union[str | None] = None

#     date: datetime = Field(
#         default_factory=datetime.now
#     )

#     description: Union[str | None] = None

# @click.command()
# @click.argument()
# def add_expense():