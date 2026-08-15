import argparse
from datetime import date
from decimal import Decimal

from src.expense_tracker.models import Expense
from src.expense_tracker.reports import (
    filter_by_month,
    total,
    total_by_category,
)
from src.expense_tracker.storage import load_expenses, save_expenses
from src.expense_tracker.utils import generate_id

DATA_FILE = "data/expenses.json"


def handle_add(args):
    expenses = load_expenses(DATA_FILE)

    expense = Expense(
        id=generate_id(expenses),
        date=date.today(),
        amount=Decimal(args.amount),
        category=args.category,
        note=args.note,
    )

    expenses.append(expense)

    save_expenses(expenses, DATA_FILE)

    print("Expense added successfully.")


def handle_list(args):
    expenses = load_expenses(DATA_FILE)

    if args.category:
        expenses = [
            expense
            for expense in expenses
            if expense.category.lower() == args.category.lower()
        ]

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"{expense.id} | "
            f"{expense.date} | "
            f"{expense.amount} | "
            f"{expense.category} | "
            f"{expense.note or ''}"
        )


def handle_summary(args):
    expenses = load_expenses(DATA_FILE)

    if args.month:
        year, month = map(int, args.month.split("-"))
        expenses = filter_by_month(expenses, year, month)

    if not expenses:
        print("No expenses found.")
        return

    print(f"Total: {total(expenses)}")
    print()

    print("By category:")
    for category, amount in total_by_category(expenses).items():
        print(f"  {category}: {amount}")


def handle_delete(args):
    expenses = load_expenses(DATA_FILE)

    original_count = len(expenses)

    expenses = [
        expense
        for expense in expenses
        if str(expense.id) != args.id
    ]

    if len(expenses) == original_count:
        print("Expense not found.")
        return

    save_expenses(expenses, DATA_FILE)

    print("Expense deleted successfully.")


def main():
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="Command-line expense tracker",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument(
        "--amount",
        required=True,
        help="Expense amount",
    )
    add_parser.add_argument(
        "--category",
        required=True,
        help="Expense category",
    )
    add_parser.add_argument(
        "--note",
        default=None,
        help="Optional note",
    )
    add_parser.set_defaults(func=handle_add)

    # list
    list_parser = subparsers.add_parser("list", help="List expenses")
    list_parser.add_argument(
        "--category",
        help="Filter by category",
    )
    list_parser.set_defaults(func=handle_list)

    # summary
    summary_parser = subparsers.add_parser(
        "summary",
        help="Display expense summary",
    )
    summary_parser.add_argument(
        "--month",
        help="Month in YYYY-MM format",
    )
    summary_parser.set_defaults(func=handle_summary)

    # delete
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete an expense",
    )
    delete_parser.add_argument(
        "--id",
        required=True,
        help="Expense ID",
    )
    delete_parser.set_defaults(func=handle_delete)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()