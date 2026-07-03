from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime

class document_pydantic(BaseModel):
    id: int
    
    name: str

    topic: Union[str | None] = None

    content: Union[str | None] = None

    created_at: datetime
    
    updated_at: Union[datetime | None] = None


class document_pydantic_input(BaseModel):
    name: str

    topic: Union[str | None] = None

    content: Union[str | None] = None 

    created_at: Union[datetime] = Field(
        default=datetime.now()
    )
    
    updated_at: Union[datetime | None] = None