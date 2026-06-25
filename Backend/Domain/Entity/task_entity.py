from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Union
@dataclass
class task_entity():
    
    task_txt: str
    description: Union[str]
    created_at: datetime
    due_time: Union[datetime]
    completed: bool
    priority: int = 1
    id: int | None = field(default=None)


    def mark_complete(self):
        self.completed = True
    
    def change_priority(self, priority: int):
        self.priority = priority

    def change_expiration(self, date: datetime):
        self.due_time = date

    def change_task_txt(self, text: str):
        self.task_txt = text

    def change_description(self, text: str):
        self.description = text  
    