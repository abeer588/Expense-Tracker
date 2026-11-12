from expenses import add_expense, filter_expenses, show_expenses, valid_date
from file_operations import export_csv, load_expenses, save_expenses


# Print a clear heading for each menu action.
def show_heading(title):
    print("\n" + "=" * 64)
    print(title.center(64))
    print("=" * 64)


# Print the numbered menu and the number of expenses.
def show_menu(expenses):
    show_heading("EXPENSE TRACKER")
    print("Record, view, and manage your everyday expenses.")
    print(f"Expenses in memory: {len(expenses)}")
    print("-" * 64)
    print("  1. Add expense")
    print("  2. Show all expenses")
    print("  3. Save expenses to JSON")
    print("  4. Open a JSON file")
    print("  5. Export expenses to CSV")
    print("  6. Filter expenses")
    print("  7. Exit")
    print("-" * 64)


# Ask for filters and print the matching expenses.
def show_filtered_expenses(expenses):
    start = input("Start date (YYYY-MM-DD, blank for any): ").strip()
    end = input("End date (YYYY-MM-DD, blank for any): ").strip()
    category = input("Category (blank for any): ").strip()
    if (start and not valid_date(start)) or (end and not valid_date(end)):
        print("Invalid date. Use YYYY-MM-DD.")
        return
    if start and end and start > end:
        print("Start date must be before or equal to end date.")
        return
    print(f"\nDates: {start or 'Any'} to {end or 'Any'}")
    print(f"Category: {category or 'Any'}")
    show_expenses(filter_expenses(expenses, start, end, category))


# Show the menu until the user chooses to exit.
def main():
    expenses = []
    while True:
        show_menu(expenses)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                show_heading("ADD EXPENSE")
                add_expense(expenses)
            elif choice == "2":
                show_heading("ALL EXPENSES")
                show_expenses(expenses)
            elif choice == "3":
                show_heading("SAVE JSON FILE")
                filename = input("JSON filename (example: expenses.json): ").strip()
                save_expenses(expenses, filename)
                print(f"Saved {len(expenses)} expense(s) to {filename}.")
            elif choice == "4":
                show_heading("OPEN JSON FILE")
                answer = input("Opening replaces the current list. Continue? (y/n): ").strip()
                if answer.lower() == "y":
                    filename = input("JSON filename: ").strip()
                    expenses = load_expenses(filename)
                    print(f"Opened {len(expenses)} expense(s) from {filename}.")
            elif choice == "5":
                show_heading("EXPORT CSV FILE")
                filename = input("CSV filename (example: expenses.csv): ").strip()
                export_csv(expenses, filename)
                print(f"Exported {len(expenses)} expense(s) to {filename}.")
            elif choice == "6":
                show_heading("FILTER EXPENSES")
                show_filtered_expenses(expenses)
            elif choice == "7":
                show_heading("EXIT")
                answer = input("Save before exiting? (y/n): ").strip()
                if answer.lower() == "y":
                    filename = input("JSON filename: ").strip()
                    save_expenses(expenses, filename)
                    print(f"Saved {len(expenses)} expense(s) to {filename}.")
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 7.")
        except (OSError, ValueError) as error:
            print(f"Could not complete that action: {error}")


if __name__ == "__main__":
    main()
