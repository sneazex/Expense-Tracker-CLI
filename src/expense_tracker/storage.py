import json
import os

# Path to the JSON file where data will be saved by defult
DATA_FILE = os.path.join("data", "expenses.json")

def load_expenses(filepath=DATA_FILE):
    """
    # Reads expenses from a JSON file.
    Returns an empty list if the file does not exist or is empty.
    """

    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_expenses(expenses, filepath=DATA_FILE):
    """
    # Saves the expense list to a JSON file.   
    """ 
    # Automatically creates the data folder if it deos not exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", endcoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)
