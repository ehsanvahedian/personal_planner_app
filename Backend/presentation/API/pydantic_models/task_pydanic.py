from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime

class task_pydantic(BaseModel):
    id: int
    task_txt: Union[str | None] = None
    description: Union[str | None] = None
    created_at: Union[datetime] = None
    due_time: Union[datetime | None] = None
    completed: Union[bool] = False
    priority: Union[int] = 1


class task_pydantic_input(BaseModel):
    task_txt: str
    description: Union[str | None] = None
    created_at: Union[datetime] = Field(default=datetime.now())
    due_time: Union[datetime | None] = None
    completed: Union[bool] = False
    priority: Union[int] = 1