from abc import ABC, abstractmethod
from Domain.Entity.task_entity import task_entity
class task_repository(ABC):
    
    @abstractmethod
    def add_task(self, task_data: task_entity): ...

    @abstractmethod
    def update_task(self, task_data: task_entity): ...

    @abstractmethod
    def delete_task(self, id: int): ...

    @abstractmethod
    def list_tasks(self): ...

    @abstractmethod
    def get_task(self, id: int) -> task_entity: ...

    def build_task(self, task_data) -> task_entity:
        try:
            return task_entity(**task_data.__dict__)
        except Exception as e:
            return {"status": "failure", "message": str(e)}   

    
    #You can add list by date
    
    #You can add list by priority


