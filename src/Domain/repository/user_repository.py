from abc import ABC, abstractmethod
from Domain.Entity.user_entity import user_entity
class user_repository(ABC):
    
    @abstractmethod
    def add_user(self, user_data: user_entity): ...

    @abstractmethod
    def update_user(self, user_data: user_entity): ...

    @abstractmethod
    def delete_user(self, id: int): ...

    @abstractmethod
    def list_users(self) -> list[user_entity]: ...

    @abstractmethod
    def get_user(self, email: int) -> user_entity: ...

    def build_user(self, user_data) -> user_entity | any:
        try:
            return user_entity(**user_data.__dict__)
        except Exception as e:
            return {"status": "failure", "message": str(e)}   

    
    #You can add list by date
    
    #You can add list by priority


