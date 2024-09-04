import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CSV_FILE = os.getenv("CSV_FILE", "expenses.csv")

# Singleton class
class ExpenseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ExpenseManager, cls).__new__(cls)
            cls._instance.initialize_csv()
        return cls._instance

    def initialize_csv(self):
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Description", "Amount"])

    def add_expense(self, date, description, amount):
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, description, amount])

    def view_expenses(self):
        expenses = []
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
        return expenses

# Factory Method for creating views of expenses
class ExpenseView:
    def __init__(self, expense_manager: ExpenseManager):
        self.expense_manager = expense_manager

    def display_expenses(self):
        expenses = self.expense_manager.view_expenses()
        for row in expenses:
            print(", ".join(row))

class Application:
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.menu()

    def menu(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                date = input("Enter the date (YYYY-MM-DD): ")
                description = input("Enter the description: ")
                amount = input("Enter the amount: ")
                self.expense_manager.add_expense(date, description, amount)
                print("Expense added successfully!")

            elif choice == "2":
                print("Expenses:")
                viewer = ExpenseView(self.expense_manager)
                viewer.display_expenses()

            elif choice == "3":
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Application()
