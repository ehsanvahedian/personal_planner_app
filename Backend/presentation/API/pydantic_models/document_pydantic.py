from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime

class document_pydantic(BaseModel):
    name: str

    topic: Union[str]
    content: Union[str | None]

    created_at: Union[datetime] = Field(
        default_factory=datetime.now
    )
    
    updated_at: Union[datetime | None]