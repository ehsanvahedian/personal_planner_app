from Infrastructure.DB.repo_implement.transaction_repo_impl import transaction_repo_impl
from Shared.database import get_session


class transactionUseCases:
    def __init__(self):
        session = get_session()
        self.implement = transaction_repo_impl(session)

    def createTransactionUseCase(self, data):
        transaction = self.implement.build_transaction(data)
        return self.implement.add_transaction(transaction)

    def updateTransactionUseCase(self, data):
        transaction = self.implement.build_transaction(data)
        return self.implement.update_transaction(transaction)

    def deleteTransactionUseCase(self, id):
        return self.implement.delete_transaction(id)

    def listTransactionsByDateUseCase(self):
        return self.implement.list_by_date()

    def listExpensesUseCase(self):
        return self.implement.list_expenses()

    def listIncomesUseCase(self):
        return self.implement.list_incomes()

    def getTransactionUseCase(self, id):
        return self.implement.get_transaction(id)