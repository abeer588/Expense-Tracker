from datetime import datetime
from decimal import Decimal, InvalidOperation
from textwrap import wrap


# Check that a date uses YYYY-MM-DD.
def valid_date(date_text):
    try:
        date = datetime.strptime(date_text, "%Y-%m-%d")
        return date.strftime("%Y-%m-%d") == date_text
    except (ValueError, TypeError):
        return False


# Check that an amount is positive and has at most two decimal places.
def valid_amount(amount_text):
    try:
        amount = Decimal(str(amount_text))
        return (amount.is_finite() and amount > 0
                and amount == amount.quantize(Decimal("0.01")))
    except (InvalidOperation, ValueError):
        return False


# Ask for an expense and add it to the list.
def add_expense(expenses):
    date = input("Date (YYYY-MM-DD): ").strip()
    if not valid_date(date):
        print("Invalid date. Expense was not added.")
        return
    category = input("Category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    amount = input("Amount: ").strip()
    if not valid_amount(amount):
        print("Enter a positive amount with at most two decimal places.")
        return
    description = input("Description: ").strip()
    expenses.append({"date": date, "category": category,
                     "amount": float(amount), "description": description})
    print("Expense added. Choose Save to keep it in a file.")


# Print expenses in a table with a total.
def show_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return
    line = "-" * 79
    print("\n" + line)
    print(f"{'Date':<10} | {'Category':<16} | {'Amount':>12} | Description")
    print(line)
    total = Decimal("0")
    for expense in expenses:
        amount = Decimal(str(expense["amount"]))
        categories = wrap(expense["category"], width=16) or [""]
        descriptions = wrap(expense["description"], width=32) or [""]
        for index in range(max(len(categories), len(descriptions))):
            date = expense["date"] if index == 0 else ""
            value = f"{amount:.2f}" if index == 0 else ""
            category = categories[index] if index < len(categories) else ""
            description = descriptions[index] if index < len(descriptions) else ""
            print(f"{date:<10} | {category:<16} | {value:>12} | {description}")
        total += amount
    print(line)
    print(f"Expenses: {len(expenses)}    Total: {total:.2f}")


# Find expenses that match the dates and category.
def filter_expenses(expenses, start_date="", end_date="", category=""):
    results = []
    for expense in expenses:
        if start_date and expense["date"] < start_date:
            continue
        if end_date and expense["date"] > end_date:
            continue
        if category and expense["category"].casefold() != category.casefold():
            continue
        results.append(expense)
    return results
