from ..ORM.transaction_ORM import TransactionType, transaction_ORM, transactions_list
from Domain.repository.transaction_repository import transaction_repository


class transaction_repo_impl(transaction_repository):
    def __init__(self, session):
        self.session = session

    def add_transaction(self, transaction_data):
        try:
            transaction = transaction_ORM(**transaction_data.__dict__)

            self.session.add(transaction)
            self.session.commit()

            return {
                "status": "success",
                "message": "transaction added"
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def update_transaction(self, transaction_data):
        try:
            res = (
                self.session.query(transaction_ORM)
                .filter(transaction_ORM.id == transaction_data.id)
                .update(transaction_data.__dict__)
            )

            self.session.commit()

            return {
                "status": "success",
                "message": str(res)
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def delete_transaction(self, id):
        try:
            res = (
                self.session.query(transaction_ORM)
                .filter(transaction_ORM.id == id)
                .delete()
            )

            self.session.commit()

            return {
                "status": "success",
                "message": f"deleted {res}"
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def get_transaction(self, id):
        try:
            return (
                self.session.query(transaction_ORM)
                .filter(transaction_ORM.id == id)
                .first()
            )

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }

    def list_by_date(self):
        try:
            return (
                self.session.query(transaction_ORM)
                .order_by(transaction_ORM.date.desc())
                .all()
            )

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }

    def list_expenses(self) -> transactions_list:
        try:

            expenses : list[transaction_ORM] = self.session.query(transaction_ORM).filter(
                    transaction_ORM.type == TransactionType.EXPENSE
                ).all()
            
            return transactions_list(
                "success",
                list(map(lambda i: i.to_entity(), expenses))
            )

        except Exception as e:
            return transactions_list("failure", str(e))

    def list_incomes(self) -> transactions_list:
        try:

            expenses : list[transaction_ORM] = self.session.query(transaction_ORM).filter(
                    transaction_ORM.type == TransactionType.INCOME
                ).all()
            
            return transactions_list(
                "success",
                list(map(lambda i: i.to_entity(), expenses))
            )

        except Exception as e:
            return transactions_list("failure", str(e))