import uuid
from datetime import date
from decimal import Decimal

import pytest

from src.expense_tracker.models import Expense


def test_create_valid_expense():
    expense = Expense(
        id=uuid.uuid4(),
        date=date(2026, 8, 4),
        amount=Decimal("12.50"),
        category="Food",
        note="Lunch"
    )

    assert isinstance(expense, Expense)
    assert expense.category == "Food"
    assert expense.amount == Decimal("12.50")
    assert expense.note == "Lunch"


def test_zero_amount_raises_value_error():
    with pytest.raises(ValueError):
        Expense(
            id=uuid.uuid4(),
            date=date.today(),
            amount=Decimal(0),
            category="Food"
        )


def test_empty_category_raises_value_error():
    with pytest.raises(ValueError):
        Expense(
            id=uuid.uuid4(),
            date=date.today(),
            amount=Decimal("10.00"),
            category=""
        )


def test_whitespace_category_raises_value_error():
    with pytest.raises(ValueError):
        Expense(
            id=uuid.uuid4(),
            date=date.today(),
            amount=Decimal("10.00"),
            category="   "
        )


def test_invalid_date_raises_type_error():
    with pytest.raises(TypeError):
        Expense(
            id=uuid.uuid4(),
            date="2026-08-04",
            amount=Decimal("10.00"),
            category="Food"
        )


def test_note_defaults_to_none():
    expense = Expense(
        id=uuid.uuid4(),
        date=date.today(),
        amount=Decimal("15.00"),
        category="Transport"
    )

    assert expense.note is None


def test_to_dict_returns_expected_dictionary():
    expense_id = uuid.uuid4()

    expense = Expense(
        id=expense_id,
        date=date(2026, 8, 4),
        amount=Decimal("12.50"),
        category="Food",
        note="Lunch"
    )

    expected = {
        "id": str(expense_id),
        "date": "2026-08-04",
        "amount": "12.50",
        "category": "Food",
        "note": "Lunch"
    }

    assert expense.to_dict() == expected


def test_from_dict_creates_expense():
    expense_id = uuid.uuid4()

    data = {
        "id": str(expense_id),
        "date": "2026-08-04",
        "amount": "12.50",
        "category": "Food",
        "note": "Lunch"
    }

    expense = Expense.from_dict(data)

    assert expense.id == expense_id
    assert expense.date == date(2026, 8, 4)
    assert expense.amount == Decimal("12.50")
    assert expense.category == "Food"
    assert expense.note == "Lunch"


def test_round_trip_serialization():
    original = Expense(
        id=uuid.uuid4(),
        date=date(2026, 8, 4),
        amount=Decimal("45.75"),
        category="Shopping",
        note="Books"
    )

    reconstructed = Expense.from_dict(original.to_dict())

    assert reconstructed == original