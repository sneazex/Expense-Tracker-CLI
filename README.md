# Expense-Tracker-CLI
## Explanation
The Expense Tracker CLI is a Python-based command-line tool built to streamline personal daily expense management. It enables users to record new expenses with categories and notes, view stored entries, filter transactions by category, remove items using their ID, and view monthly spending summaries. All records are stored locally in a JSON file to ensure data persistence.
## Features
- **Add Expense:** Log new expenses with amount, category, and notes (`add`).
- **List Expenses:** View all recorded expenses or filter them by a specific category (`list`).
- **Monthly Summary:** Generate total spending reports for a specific month (`summary`).
- **Delete Expense:** Remove a specific expense entry using its unique ID (`delete`).
- **Data Persistence:** Automatically save all records to a local JSON file.

> **Note:** The data/expenses.json file contains real personal data and is excluded via .gitignore — only the sample file (expenses_sample.json) is tracked in the repository.
## Installation
**Requirements:**
- Python 3.7 or higher

1. **Clone the Repository:**
```bash
   git clone https://github.com/sneazex/Expense-Tracker-CLI.git
   cd Expense-Tracker-CLI
```
2. **Create and Activate a Virtual Environment:**
```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS and Linux:
   source .venv/bin/activate
```
   ## Usage
Run the commands below using `main.py`:

 **Add an expense:**
```bash
  python main.py add --amount 12.50 --category food --note "Lunch"
```
**List all expenses:**
```bash
python main.py list
```
**List expenses by category:**
```bash
python main.py list --category food
```
**View monthly summary:**
```bash
python main.py summary --month 2026-08
```
**Delete an expense by ID:**
```bash
python main.py delete --id 3
```
## Project Structure
```text
Expense-Tracker-CLI/
├── .gitignore
├── README.md
├── requirements.txt
├── LICENSE
├── main.py
├── data/
│   └── expenses_sample.json
├── src/
│   └── expense_tracker/
│       ├── __init__.py
│       ├── models.py
│       ├── storage.py
│       ├── reports.py
│       ├── cli.py
│       └── utils.py
└── tests/
    ├── __init__.py
    ├── test_models.py
    ├── test_storage.py
    └── test_reports.py
