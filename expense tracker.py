import json
import os

# Initialize an empty expense data structure
expenses = {
    "categories": [],
    "transactions": []
}

# Define file paths for data storage
data_file = "expenses.json"

# Load existing data from a JSON file if it exists
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        expenses = json.load(file)

# Function to add a new expense
def add_expense():
    category = input("Enter the expense category: ")
    amount = float(input("Enter the expense amount: "))
    expenses["transactions"].append({"category": category, "amount": amount})
    print("Expense added successfully!")

# Function to view expenses by category
def view_expenses_by_category():
    category = input("Enter the category to view expenses: ")
    total = 0
    for expense in expenses["transactions"]:
        if expense["category"] == category:
            print(f"{expense['category']}: ${expense['amount']:.2f}")
            total += expense["amount"]
    print(f"Total {category} expenses: ${total:.2f}")

# Function to generate a basic financial report
def generate_report():
    print("Financial Report")
    for category in expenses["categories"]:
        total = sum(expense["amount"] for expense in expenses["transactions"] if expense["category"] == category)
        print(f"{category}: ${total:.2f}")
    total_expenses = sum(expense["amount"] for expense in expenses["transactions"])
    print(f"Total Expenses: ${total_expenses:.2f}")

# Main loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses by Category")
    print("3. Generate Financial Report")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses_by_category()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        # Save data to the JSON file before quitting
        with open(data_file, "w") as file:
            json.dump(expenses, file)
        print("Expense data saved. Exiting.")
        break
    else:
        print("Invalid choice. Please try again.")
