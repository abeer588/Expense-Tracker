# Expense Tracker

A Python console project for recording everyday expenses.

## Features

- Add an expense with a date, category, amount, and description.
- Show expenses in a table with column headings, a count, and a total.
- Save expenses to a JSON file.
- Open an existing JSON expense file.
- Export expenses to a CSV file for Microsoft Excel.
- Filter by date range, category, or both.

## Program plan

The program shows a numbered menu and repeats until the user chooses to exit. Expenses are stored as a list of dictionaries.

Files:

- `main.py`: display the menu and handle choices.
- `expenses.py`: add, display, and filter expenses.
- `file_operations.py`: load JSON, save JSON, and export CSV.
- `.gitignore`: ignore Python cache files, local settings, and personal expense files.

Dates use `YYYY-MM-DD`. Date filters include both the start and end dates. Leave a filter blank to skip it. Category matching ignores capital letters and matches the whole category.

## How to run

Install Python 3. Open a terminal in this folder and run:

```bash
python main.py
```

If your computer uses `python3`, run `python3 main.py` instead.

## How to use

1. Choose `1` to add an expense, for example `2026-11-09`, `Food`, `12.50`, and `Lunch`.
2. Choose `2` to show the expenses.
3. Choose `3` and enter `expenses.json` to save.
4. Choose `4` to open a saved file. This replaces the current list after confirmation.
5. Choose `5` and enter `expenses.csv` to export all expenses for Excel.
6. Choose `6` to filter expenses. For example, enter `2026-11-01`, `2026-11-30`, and `Food`.
7. Choose `7` to exit. The program offers to save first.

Saving or exporting to an existing filename overwrites that file. Files are created in the current terminal folder unless a full path is entered. Data is saved only when you choose Save or save before exiting. CSV export includes all expenses; filters only change the console display.

## Current status

The planned features are implemented. Short comments above every function explain its purpose.

## Next step

Run the program and check each menu option. Try invalid dates, negative amounts, missing files, and date ranges with matching and nonmatching expenses.

## Repository progress

Make commits as you complete and understand real changes. Do not create artificial progress commits for code already finished. Possible milestones for your own development are the menu, adding and showing expenses, JSON files, CSV export, filters, and testing/documentation.

The assignment requests a website URL. If your instructor expects a repository link, submit your repository URL after uploading your work. This project runs in a terminal; GitHub Pages does not run this Python application.

## Console appearance

The menu has clear headings and shows how many expenses are in memory.
Each action has its own heading. Expense lists use Date, Category, Amount,
and Description columns. Long categories and descriptions wrap onto extra
lines. Filter results show the chosen dates and category above the table.
Save, open, and export messages show the filename and expense count.
No extra packages or terminal color settings are needed.

