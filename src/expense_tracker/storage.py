import json
import os
from src.expense_tracker.models import Expense

DATA_FILE = os.path.join("data", "expenses.json")

def load_expenses(filepath=DATA_FILE):
    """
    Returns a list of Expense objects from the JSON file.
    Returns an empty list if the file does not exist or is empty.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Expense.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, TypeError):
        return []

def save_expenses(filepath=DATA_FILE, expenses=None):
    """
    Saves a list of Expense objects to a JSON file.
    """
    if expenses is None:
        expenses = []

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        data = [expense.to_dict() for expense in expenses]
        json.dump(data, f, indent=4)