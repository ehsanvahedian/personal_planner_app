from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

class document_ORM(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    topic: Mapped[str] = mapped_column(nullable=True)
    content: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime] = mapped_column(nullable=True)