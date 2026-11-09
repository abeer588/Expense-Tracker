from expenses import add_expense, filter_expenses, show_expenses, valid_date
from file_operations import export_csv, load_expenses, save_expenses


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
    show_expenses(filter_expenses(expenses, start, end, category))


# Show the menu until the user chooses to exit.
def main():
    expenses = []
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Save JSON file")
        print("4. Open JSON file")
        print("5. Export CSV file")
        print("6. Filter expenses")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_expense(expenses)
            elif choice == "2":
                show_expenses(expenses)
            elif choice == "3":
                filename = input("JSON filename (example: expenses.json): ").strip()
                save_expenses(expenses, filename)
                print("Expenses saved.")
            elif choice == "4":
                answer = input("Opening replaces the current list. Continue? (y/n): ").strip()
                if answer.lower() == "y":
                    filename = input("JSON filename: ").strip()
                    expenses = load_expenses(filename)
                    print("Expenses opened.")
            elif choice == "5":
                filename = input("CSV filename (example: expenses.csv): ").strip()
                export_csv(expenses, filename)
                print("Expenses exported.")
            elif choice == "6":
                show_filtered_expenses(expenses)
            elif choice == "7":
                answer = input("Save before exiting? (y/n): ").strip()
                if answer.lower() == "y":
                    filename = input("JSON filename: ").strip()
                    save_expenses(expenses, filename)
                    print("Expenses saved.")
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 7.")
        except (OSError, ValueError) as error:
            print(f"Could not complete that action: {error}")


if __name__ == "__main__":
    main()
