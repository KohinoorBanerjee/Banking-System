class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")


def main():
    accounts = {}

    while True:
        print("\n🏦 Banking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            acc_no = input("Enter account number: ")
            name = input("Enter name: ")
            if acc_no in accounts:
                print("Account already exists.")
            else:
                accounts[acc_no] = Account(acc_no, name)
                print("Account created successfully!")

        elif choice == '2':
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                amt = float(input("Enter amount to deposit: "))
                accounts[acc_no].deposit(amt)
            else:
                print("Account not found.")

        elif choice == '3':
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                amt = float(input("Enter amount to withdraw: "))
                accounts[acc_no].withdraw(amt)
            else:
                print("Account not found.")

        elif choice == '4':
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                accounts[acc_no].display()
            else:
                print("Account not found.")

        elif choice == '5':
            print("Thank you for using the banking system!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
