def generate_id(expenses) :
    if not expenses:
        return 1

    return sum(expense.id for expense in expenses) + 1
