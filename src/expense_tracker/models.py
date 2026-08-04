from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any, Self
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

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "date": self.date.isoformat(),
            "amount": str(self.amount),
            "category": self.category,
            "note": self.note
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            id=UUID(data["id"]),
            date=date.fromisoformat(data.get("date")),
            amount=Decimal(data.get("amount")),
            category=data.get("category"),
            note=data.get("note")
        )