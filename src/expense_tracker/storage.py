import json
import os

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
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(filepath, expenses):
    """
    Saves the expense list to a JSON file.
    Automatically creates the data folder if it does not exist.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Expense nesneleri geldiyse to_dict() ile JSON'ın yazabileceği dict formatına çevirir
    data_to_save = [
        exp.to_dict() if hasattr(exp, "to_dict") else exp
        for exp in expenses
    ]

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, indent=4, ensure_ascii=False)