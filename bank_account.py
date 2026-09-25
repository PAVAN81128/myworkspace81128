# Start with an account balance of ₹10,000.
balance = 10000

# Keep showing the menu until the user chooses to exit.
while True:
    print("===== BANK ACCOUNT =====")
    print()
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print()

    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        # Show the current balance.
        print(f"Your current balance is ₹{balance}")

    elif choice == "2":
        # Ask for a deposit and add it if the amount is positive.
        amount = int(input("Enter deposit amount: "))
        print()

        if amount > 0:
            balance = balance + amount
            print(f"₹{amount} deposited successfully.")
            print(f"Your new balance is ₹{balance}")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        # Ask for a withdrawal and check that it is valid and affordable.
        amount = int(input("Enter withdrawal amount: "))
        print()

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > balance:
            print("Insufficient balance.")
            print(f"Your current balance is ₹{balance}")
        else:
            balance = balance - amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Your remaining balance is ₹{balance}")

    elif choice == "4":
        print("Thank you for using our bank.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    print()