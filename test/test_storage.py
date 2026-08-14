import os
from datetime import date
import pytest
from src.expense_tracker.storage import load_expenses, save_expenses
from src.expense_tracker.models import Expense

TEST_FILE = os.path.join("data", "test_expenses.json")

@pytest.fixture(autouse=True)
def cleanup():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_load_non_existent_file():
    result = load_expenses(TEST_FILE)
    assert result == []

def test_save_and_load_expenses():
    test_uuid = "123e4567-e89b-12d3-a456-426614174000"
    sample_expense = Expense(id=test_uuid, date=date(2026, 8, 14), amount=12.5, category="food", note="lunch")
    save_expenses(TEST_FILE, [sample_expense])
    assert os.path.exists(TEST_FILE)

    loaded_data = load_expenses(TEST_FILE)
    assert len(loaded_data) == 1
    # id nesnesini string'e çevirip kontrol ediyoruz
    assert str(loaded_data[0].id) == test_uuid
    assert loaded_data[0].amount == 12.5