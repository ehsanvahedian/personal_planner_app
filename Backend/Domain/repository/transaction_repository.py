from abc import ABC, abstractmethod
from Domain.Entity.transaction_entity import transaction_entity
class transaction_repository(ABC):
    
    @abstractmethod
    def add_transaction(self, transaction_data: transaction_entity): ...

    @abstractmethod
    def update_transaction(self, transaction_data: transaction_entity): ...

    @abstractmethod
    def delete_transaction(self, transaction_data: transaction_entity): ...

    @abstractmethod
    def list_by_date(self): ...

    @abstractmethod
    def list_incomes(self): ...

    @abstractmethod
    def list_expenses(self): ...


    def biuld_transaction(self, transaction_data: transaction_entity) -> transaction_entity:
        return transaction_entity(**transaction_data.__dict__)
    
    #You can add list by date
    
    #You can add list by priority


