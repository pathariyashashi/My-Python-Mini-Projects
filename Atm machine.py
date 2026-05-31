class ATM:

    # Constructor
    def __init__(self, name, pin, balance):

        self.name = name
        self.__pin = pin
        self.__balance = balance
        self.transactions = []

    # PIN Verify
    def verify_pin(self, entered_pin):

        if entered_pin == self.__pin:
            return True
        else:
            return False

    # Deposit Method
    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount

            self.transactions.append(f"Deposited ₹{amount}")

            print(f"₹{amount} deposited successfully.")

        else:
            print("Invalid Amount!")

    # Withdraw Method
    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            self.transactions.append(f"Withdraw ₹{amount}")

            print(f"₹{amount} withdrawn successfully.")

        else:
            print("Insufficient Balance!")

    # Balance Inquiry
    def check_balance(self):

        print(f"Current Balance: ₹{self.__balance}")

    # Mini Statement
    def mini_statement(self):

        print("\n----- Mini Statement -----")

        if len(self.transactions) == 0:
            print("No Transactions Yet")

        else:
            for t in self.transactions:
                print(t)

    # ATM Menu
    def menu(self):

        print(f"\nWelcome {self.name}")

        pin = int(input("Enter ATM PIN: "))

        if self.verify_pin(pin):

            while True:

                print("\n===== ATM MENU =====")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Exit")

                choice = int(input("Enter Choice: "))

                # Deposit
                if choice == 1:

                    amount = int(input("Enter Amount: "))
                    self.deposit(amount)

                # Withdraw
                elif choice == 2:

                    amount = int(input("Enter Amount: "))
                    self.withdraw(amount)

                # Balance
                elif choice == 3:

                    self.check_balance()

                # Mini Statement
                elif choice == 4:

                    self.mini_statement()

                # Exit
                elif choice == 5:

                    print("Thank You For Using ATM")
                    break

                else:
                    print("Invalid Choice!")

        else:
            print("Wrong PIN!")


# Object Creation
user1 = ATM("Shashi", 1234, 5000)

# Start ATM
user1.menu()