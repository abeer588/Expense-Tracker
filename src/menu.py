from expenses import add_expense, filter_expenses, show_expenses, valid_date
from file_operations import export_csv, load_expenses, save_expenses


# Print the choices available to the user.
def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Save expenses to JSON")
    print("4. Open a JSON file")
    print("5. Export expenses to CSV")
    print("6. Filter expenses")
    print("7. Exit")


# Ask where to save the expense list and write it as JSON.
def save_to_file(expenses):
    filename = input("JSON filename: ").strip()
    save_expenses(expenses, filename)
    print(f"Saved {len(expenses)} expense(s) to {filename}.")


# Ask for a CSV filename and export all expenses for Excel.
def export_to_file(expenses):
    filename = input("CSV filename: ").strip()
    export_csv(expenses, filename)
    print(f"Exported {len(expenses)} expense(s) to {filename}.")


# Ask for optional dates and a category, then print matching expenses.
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

    matches = filter_expenses(expenses, start, end, category)
    show_expenses(matches)


# Keep showing the menu and run the action the user chooses.
def run_menu():
    expenses = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_expense(expenses)
            elif choice == "2":
                show_expenses(expenses)
            elif choice == "3":
                save_to_file(expenses)
            elif choice == "4":
                answer = input("Replace the current list? (y/n): ").strip().lower()
                if answer == "y":
                    filename = input("JSON filename: ").strip()
                    expenses = load_expenses(filename)
                    print(f"Opened {len(expenses)} expense(s) from {filename}.")
            elif choice == "5":
                export_to_file(expenses)
            elif choice == "6":
                show_filtered_expenses(expenses)
            elif choice == "7":
                answer = input("Save before exiting? (y/n): ").strip().lower()
                if answer == "y":
                    save_to_file(expenses)
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 7.")
        except (OSError, ValueError) as error:
            print(f"Could not complete that action: {error}")
