from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from Domain.Entity.document_entity import document_entity
from dataclasses import dataclass
class document_ORM(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    topic: Mapped[str] = mapped_column(nullable=True)
    content: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime] = mapped_column(nullable=True)


    def to_entity(self) -> document_entity:
        return document_entity(
            name=self.name,
            topic=self.topic,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at,
            id=self.id
        )
    
@dataclass 
class documents_list:
    status: str
    ducuments: list[document_entity] = None
    message: str = None