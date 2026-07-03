from dataclasses import dataclass

@dataclass
class Money:
    amount: int | None
    currency: str | None

    def add(self, amount):
        self.amount += amount

    def subtract(self, amount):
        self.amount -= amount

    def is_positive(self):
        return True if self.amount > 0 else False
    
    def to_dict(self):
        return {
            "amount": self.amount,
            "currency": self.currency,
        }