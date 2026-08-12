import os
import pytest
from src.expense_tracker.storage import load_expenses, save_expenses

# temporary file path
TEST_FILE = os.path.join("data", "test_expenses.json")

@pytest.fixture(autouse=True)
def cleanup():
    #Cleanup before and after each test
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_load_non_existent_file():
    # Test loading from a non-existent file
    result = load_expenses(TEST_FILE)
    assert result == []

def test_save_and_load_expenses():
    # Test saving and loading expenses
    sample_data = [{"id": 1, "amount": 12.5, "category": "food", "note": "lunch"}]
    save_expenses(TEST_FILE, sample_data)
    assert os.path.exists(TEST_FILE) # Check if file was created

    loaded_data = load_expenses(TEST_FILE)
    assert loaded_data == sample_data #Check if loaded data matches saved data