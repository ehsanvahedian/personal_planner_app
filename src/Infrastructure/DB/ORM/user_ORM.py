from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from .Base import Base
from Domain.Entity.user_entity import user_entity
from dataclasses import dataclass, field


class user_ORM(Base):
    __tablename__ = "users"


    email: Mapped[str] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(nullable=True)
    signup_at: Mapped[datetime]
    password: Mapped[str] = mapped_column(nullable=True)

    def to_entity(self):
        return user_entity(
            email=self.email,
            user_name=self.user_name,
            signup_at=self.signup_at,
            password=self.password
        )
    

@dataclass
class users_list:
    status: str
    message: str | None = field(default=None)
    users: list[user_entity] | None = field(default=None)