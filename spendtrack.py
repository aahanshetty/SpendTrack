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
        print("View Spending by Category selected")

    elif choice == "5":
        print("Exiting SpendTrack")
        break

    else:
        print("Invalid choice")
        print()