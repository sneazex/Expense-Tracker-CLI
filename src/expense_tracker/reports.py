from collections import defaultdict

def total(expenses):
    return sum(e.amount for e in expenses)

def total_by_category(expenses):
    totals = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.amount
    return dict(totals)

def filter_by_month(expenses, year, month):
    return [
        e for e in expenses
        if e.date.year == year and e.date.month == month
    ]