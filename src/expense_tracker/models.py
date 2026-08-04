from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID


@dataclass
class Expense:
    id: UUID
    date: date
    amount: Decimal
    category: str
    note: str | None = None

    def __post_init__(self):
        if not isinstance(self.date, date):
            raise TypeError("A valid calendar date is required")

        if self.amount == 0:
            raise ValueError("Expense amount cannot be zero")

        if not self.category or not self.category.strip():
            raise ValueError("Category cannot be empty")
