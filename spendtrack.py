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
        amount = float(input("Enter amount: $"))
        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

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
                    expense["amount"],
                    "|",
                    expense["category"]
                )

        print()

    elif choice == "3":
        print("View Total Spending selected")

    elif choice == "4":
        print("View Spending by Category selected")

    elif choice == "5":
        print("Exiting SpendTrack")
        break

    else:
        print("Invalid choice")