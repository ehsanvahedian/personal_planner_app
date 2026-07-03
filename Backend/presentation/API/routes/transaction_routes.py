from fastapi import APIRouter, Depends, Body

from Application.UseCases.transactionUseCases import transactionUseCases
from ..pydantic_models.transaction_pydantic import transaction_pydantic, transaction_pydantic_input
from typing import Annotated

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

TUC = transactionUseCases()

@router.post("/add")
async def add_transaction(
    input_data: Annotated[transaction_pydantic_input, Depends(transaction_pydantic_input)]
):
    input_data.fix_amount()
    data = input_data
    return TUC.createTransactionUseCase(data)

@router.put("/update")
async def update_transaction(
    data: Annotated[transaction_pydantic, Depends(transaction_pydantic)]
):
    data.fix_amount()
    return TUC.updateTransactionUseCase(data)

@router.delete("/{id}")
async def delete_transaction(id: int):
    return TUC.deleteTransactionUseCase(id)

@router.get("/")
async def list_transactions():
    return TUC.listTransactionsByDateUseCase()

@router.get("/expenses")
async def list_expenses():
    return TUC.listExpensesUseCase()

@router.get("/incomes")
async def list_incomes():
    return TUC.listIncomesUseCase()