# Expense Tracker

A Python console program for adding, viewing, saving, opening, exporting, and filtering expenses.

## Run the program

Open a terminal in the `ExpenseTracker` folder. Run:

```bash
python src/main.py
```

If your computer uses `python3`, run `python3 src/main.py`. The program uses the Python standard library.

## What each file does

| File | Purpose |
| --- | --- |
| `src/main.py` | Starts the program by calling `run_menu()`. |
| `src/menu.py` | Shows the menu, reads your choice, and calls the right function. |
| `src/expenses.py` | Adds, prints, and filters expenses. It also checks dates and amounts. |
| `src/file_operations.py` | Saves and opens JSON files and exports CSV files. |

## Try it

1. Choose **4**, enter **y**, and type `expenses_tracker.json` to open the included expense file.
2. Choose **2** to print all expenses, or **1** to add an expense. Enter dates as `YYYY-MM-DD`.
3. Choose **6** to filter expenses. You can enter a start date, an end date, a category, or any combination. Leave an input blank to skip it. The dates are inclusive and category matching ignores capitalization.
4. Choose **3** to save to a JSON file such as `expenses.json`.
5. Choose **5** to export all expenses to a CSV file such as `expenses.csv`. Open that file in Excel. The included `tracker.csv` shows the export format.
6. Choose **7** to exit. The program asks whether you want to save first.

Filenames are relative to the terminal's current folder. Saving or exporting to an existing filename replaces that file.
