
import json
from datetime import datetime
import os

EXPENSE_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    print("\n  Add Expense\n")

    amount = input(" Enter amount: ").strip()
    category = input(" Enter category: ").strip()
    date = input(" Enter date (YYYY-MM-DD): ").strip()

    try:
        amount = float(amount)
    except:
        print("\n\033[91m Invalid amount! \033[0m\n")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except:
        print("\n\033[91m Invalid date format! Use YYYY-MM-DD. \033[0m\n")
        return

    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "date": date})
    save_expenses(expenses)

    print("\n\033[92m Expense added successfully! \033[0m\n")

def view_expenses():
    print("\n  All Expenses\n")
    expenses = load_expenses()

    if not expenses:
        print(" No expenses found.\n")
        return

    for i, e in enumerate(expenses, start=1):
        print(f" {i}. Amount: {e['amount']} | Category: {e['category']} | Date: {e['date']}")
    print()

def summarize_by_category():
    print("\n  Summary by Category\n")
    expenses = load_expenses()

    if not expenses:
        print(" No expenses found.\n")
        return

    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + float(e["amount"])

    for cat, total in summary.items():
        print(f" {cat}: {total}")

    print()

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize by Category")
        print("4. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_by_category()
        elif choice == "4":
            print("\nExiting application...\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main()
