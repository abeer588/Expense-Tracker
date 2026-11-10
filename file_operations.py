import csv
import json

from expenses import valid_amount, valid_date


# Save all expenses to a JSON file.
def save_expenses(expenses, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, allow_nan=False)


# Open a JSON file and check its expense data.
def load_expenses(filename):
    with open(filename, "r", encoding="utf-8") as file:
        expenses = json.load(file)
    if not isinstance(expenses, list):
        raise ValueError("The file must contain a list of expenses.")
    for expense in expenses:
        if not isinstance(expense, dict):
            raise ValueError("Each expense must be a dictionary.")
        if set(expense) != {"date", "category", "amount", "description"}:
            raise ValueError("An expense has missing or extra fields.")
        if not valid_date(expense["date"]):
            raise ValueError("An expense has an invalid date.")
        if not isinstance(expense["category"], str) or not expense["category"].strip():
            raise ValueError("An expense has an invalid category.")
        if isinstance(expense["amount"], bool) or not isinstance(expense["amount"], (int, float)):
            raise ValueError("An expense amount must be a number.")
        if not valid_amount(expense["amount"]):
            raise ValueError("An expense has an invalid amount.")
        if not isinstance(expense["description"], str):
            raise ValueError("An expense has an invalid description.")
    return expenses


# Export all expenses to a CSV file for Excel.
def export_csv(expenses, filename):
    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "category", "amount", "description"])
        for expense in expenses:
            writer.writerow([expense["date"], expense["category"],
                             f"{expense['amount']:.2f}", expense["description"]])
