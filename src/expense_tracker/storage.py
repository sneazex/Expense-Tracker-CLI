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
            expenses = []
            for item in data:
                if isinstance(item, dict):
                    # id sayı bile gelse stringe çevirip güvene alıyoruz
                    if "id" in item and not isinstance(item["id"], str):
                        item["id"] = str(item["id"])
                    expenses.append(Expense.from_dict(item))
                else:
                    expenses.append(item)
            return expenses
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(filepath, expenses):
    """
    Saves the expense list to a JSON file.
    Automatically creates the data folder if it does not exist.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    data_to_save = [
        exp.to_dict() if hasattr(exp, "to_dict") else exp
        for exp in expenses
    ]

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, indent=4, ensure_ascii=False)