from dataclasses import dataclass, replace
from datetime import datetime
from typing import Union
@dataclass
class user_entity():
    
    email: str
    user_name: Union[str]
    signup_at: datetime
    password: Union[str]

    def auth_password(self, password):
        return self.password == password
    
    def replace_items(self, updated_data):
        return replace(self, **updated_data)