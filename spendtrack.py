import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

except FileNotFoundError:
    expenses = []


while True:
    print("=========================")
    print("       SPENDTRACK")
    print("=========================")
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter amount: $"))

            if amount <= 0:
                print("Amount must be greater than $0.")
                print()
                continue

        except ValueError:
            print("Invalid amount. Please enter a number.")
            print()
            continue

        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense added successfully.")
        print()

    elif choice == "2":
        print()
        print("------ Expenses ------")

        if len(expenses) == 0:
            print("No expenses have been added.")

        else:
            for expense in expenses:
                print(
                    expense["name"],
                    "| $",
                    format(expense["amount"], ".2f"),
                    "|",
                    expense["category"]
                )

        print()

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print()
        print("Total Spending: $", format(total, ".2f"))
        print()

    elif choice == "4":
        print()
        print("------ Spending by Category ------")

        if len(expenses) == 0:
            print("No expenses have been added.")

        else:
            category_totals = {}

            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]

                if category in category_totals:
                    category_totals[category] = category_totals[category] + amount

                else:
                    category_totals[category] = amount

            for category in category_totals:
                print(
                    category,
                    "| $",
                    format(category_totals[category], ".2f")
                )

        print()

    elif choice == "5":
        print("Exiting SpendTrack")
        break

    else:
        print("Invalid choice")
        print()