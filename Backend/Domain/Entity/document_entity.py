from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class document_entity:
    name: str
    topic: str
    content: str
    created_at: datetime
    updated_at: datetime
    id: int | None = field(default=None)
    
    def update_date(self, date: datetime):
        self.updated_at = date
