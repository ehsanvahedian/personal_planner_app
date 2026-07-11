from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from .Base import Base
from Domain.Entity.task_entity import task_entity
from dataclasses import dataclass, field


class task_ORM(Base):
    __tablename__ = "tasks"


    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task_txt: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime]
    due_time: Mapped[datetime] = mapped_column(nullable=True)
    completed: Mapped[bool] = mapped_column(nullable=True)
    priority: Mapped[int] = mapped_column(nullable=True)
   
    def to_entity(self):
        return task_entity(
            id=self.id,
            task_txt=self.task_txt,
            description=self.description,
            created_at=self.created_at,
            due_time=self.due_time,
            completed=self.completed,
            priority=self.priority,
        )
    

@dataclass
class tasks_list:
    status: str
    message: str | None = field(default=None)
    pending: list[task_entity] | None = field(default=None)
    completed: list[task_entity] | None = field(default=None)