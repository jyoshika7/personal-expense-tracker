expenses = []


def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                expense = {
                    "date": data[0],
                    "category": data[1],
                    "amount": float(data[2]),
                    "description": data[3]
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass


def save_expense(expense):
    with open("expenses.txt", "a") as file:
        file.write(
            f"{expense['date']}|"
            f"{expense['category']}|"
            f"{expense['amount']}|"
            f"{expense['description']}\n"
        )


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expense(expense)

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n----- EXPENSES -----")

    for expense in expenses:
        print(
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['description']}"
        )


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal expenses: ₹{total:.2f}")


def main():
    load_expenses()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()