import typer
from typing import Annotated
from presentation.pydantic_models.transaction_pydantic import transaction_pydantic_input, TransactionType
from Application.UseCases.transactionUseCases import transactionUseCases
TUC = transactionUseCases()


transaction_app = typer.Typer()


# return help while execute transaction_app
@transaction_app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())
        raise typer.Exit()
    

@transaction_app.command()
def add(
        amount: Annotated[int, typer.Argument(help="integer")] = None,
        type: Annotated[str, typer.Argument(help="'i' or 'income' | 'e' or 'expense'")] = None,
        c: Annotated[bool, typer.Option()] = False
    ):
    """arguments: amount(int),type('i' or 'income' | 'e' or 'expense') options: -c 'for more detailed transaction'"""
    try:    
        if c:
            # if detailed transaction handle data recieving:
            amount = input("amount:  (empty for None) ")
            type = input("type: ('i' or 'income' | 'e' or 'expense')")
            if type in ["i", "income"]:
                type = TransactionType.INCOME
            elif type in ["e", "expense"]:
                type = TransactionType.EXPENSE
            else:
                raise ValueError("Enter a valid value: 'i' or 'income' | 'e' or 'expense'")
            title = input("title:  (empty for None) ") and None
            source = input("source: (empty for None) ") and None
            datetime = input("Enter the due time 'Y/m/d': ")

            # You can add hour later

            datetime = datetime.strptime(datetime, "%Y/%m/%d") if datetime else None
            description = input("description:  (empty for None) ") and None
            data = transaction_pydantic_input(title=title,amount=amount, type=type, source=source, date=datetime,description=description)
            TUC.createTransactionUseCase(data)
            print("Transaction added")
            return
        
        if type in ["i", "income"]:
            transaction_type = TransactionType.INCOME
        elif type in ["e", "expense"]:
            transaction_type = TransactionType.EXPENSE
        else:
            raise ValueError("Enter a valid value: 'i' or 'income' | 'e' or 'expense'")
        
        data = transaction_pydantic_input(amount=amount, type=transaction_type) #create the pydantic type for appropriate app entry
        TUC.createTransactionUseCase(data)
        print("Transaction added")


    except Exception as e:
        print("error: ", str(e))


# @transaction_app.command()
# def update(
#     id: Annotated[int, typer.Argument()]
# ):
#     """update 'id'"""
#     try:
#         TUC.markTaskCompleteUseCase(id)
#         print("You've done the task.")
#     except Exception as e:
#         print("Error: ", str(e))


@transaction_app.command()
def get():
    """This will list transactions."""
    try:
        expenses = TUC.listExpensesUseCase()
        incomes = TUC.listIncomesUseCase()

        if not expenses and not incomes:
            print("no transaction")
            return
        
        print("expenses: \n")
        for i in expenses.transactions:
            print(f"\t id: {i.id}: {i.amount}, for{i.title}, in: {i.date}, to: {i.source}, detail: {i.description}")
        for i in incomes.transactions:
            print(f"\t id: {i.id}: {i.amount}, for{i.title}, in: {i.date}, from: {i.source}, detail: {i.description}")
            
    except Exception as e:
        print("Error: ", str(e))


@transaction_app.command()
def delete(
    id: Annotated[int, typer.Argument()]
):
    """delete 'id'"""
    confirm =typer.confirm("Are you sure you want to delete this transaction? ", default=True)
    try:
        if confirm:
            res = TUC.deleteTransactionUseCase(id)
            if res["status"] == "success":
                print("transaction deleted")
                return
            print("no transaction with this id")
    except Exception as e:
        print("Error: ", str(e))