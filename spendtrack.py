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
    print("Add Expense selected")

elif choice == "2":
    print("View Expenses selected")

elif choice == "3":
    print("View Total Spending selected")

elif choice == "4":
    print("View Spending by Category selected")

elif choice == "5":
    print("Exiting SpendTrack")

else:
    print("Invalid choice")