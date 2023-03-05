from src.user import User

class Customer(User):
    def __init__(self, name, email, password, account_number):
        super().__init__(name, email, password)
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(self.account_number, amount, "Deposit")
        transaction.save_transaction()

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            transaction = Transaction(self.account_number, amount, "Withdraw")
            transaction.save_transaction()

    def view_balance(self):
        print(f"Your balance is {self.balance}")

    def view_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

