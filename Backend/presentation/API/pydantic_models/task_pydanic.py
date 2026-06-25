from pydantic import BaseModel
from typing import Union
from datetime import datetime

class task_pydantic(BaseModel):
    task_txt: str
    description: Union[str | None] = None
    created_at: Union[datetime] = datetime.now()
    due_time: Union[datetime | None] = None
    completed: Union[bool] = False
    priority: Union[int] = 1

class update_task_pydantic(BaseModel):
    id: int
    task_txt: str
    description: Union[str | None] = None
    created_at: Union[datetime] = datetime.now()
    due_time: Union[datetime | None] = None
    completed: Union[bool] = False
    priority: Union[int] = 1