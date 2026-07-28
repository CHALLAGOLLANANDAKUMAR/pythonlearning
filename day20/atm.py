pin = 1234
balance = 10000

entered_pin = int(input("Enter ATM PIN: "))

if entered_pin == pin:

    while True:

        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            print("Available Balance =", balance)

        elif choice == 2:
            amount = int(input("Enter Deposit Amount: "))
            balance += amount
            print("Amount Deposited Successfully")
            print("Balance =", balance)

        elif choice == 3:
            amount = int(input("Enter Withdraw Amount: "))

            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance =", balance)
            else:
                print("Insufficient Balance")

        elif choice == 4:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

else:
    print("Wrong PIN")
