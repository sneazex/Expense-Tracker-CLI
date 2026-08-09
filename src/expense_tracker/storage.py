import json
import os

from src.expense_tracker.models import Expense

DATA_FILE = os.path.join("data", "expenses.json")


def load_expenses(filepath=DATA_FILE):
    """
    Reads expenses from a JSON file.
    Returns an empty list if the file does not exist or is empty.
    """

    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [Expense.from_dict(item) for item in data]

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses, filepath=DATA_FILE):
    """
    Saves the expense list to a JSON file.
    """

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    data = [expense.to_dict() for expense in expenses]

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)