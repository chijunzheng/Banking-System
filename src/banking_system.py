import os

def login(username, password):
    """
    This function takes in the username and password entered by the user and returns True if they are valid.
    """
    with open('users.txt', 'r') as f:
        for line in f:
            if line.strip() == username + ' ' + password:
                return True
    return False

def create_account():
    """
    This function creates a new account and stores it in the accounts.txt file.
    """
    name = input("Enter your name: ")
    account_number = int(input("Enter your account number: "))
    balance = int(input("Enter your balance: "))

    with open('accounts.txt', 'a') as f:
        f.write(f"{name} {account_number} {balance}\n")

    print("Account created successfully!")

def deposit():
    """
    This function deposits money into an account.
    """
    account_number = int(input("Enter your account number: "))
    amount = int(input("Enter the amount to be deposited: "))

    with open('accounts.txt', 'r') as f:
        lines = f.readlines()

    with open('accounts.txt', 'w') as f:
        for line in lines:
            data = line.split()
            if int(data[1]) == account_number:
                data[2] = str(int(data[2]) + amount)
                f.write(' '.join(data) + '\n')
            else:
                f.write(line)

    print("Amount deposited successfully!")

def withdraw():
    """
    This function withdraws money from an account.
    """
    account_number = int(input("Enter your account number: "))
    amount = int(input("Enter the amount to be withdrawn: "))

    with open('accounts.txt', 'r') as f:
        lines = f.readlines()

    with open('accounts.txt', 'w') as f:
        for line in lines:
            data = line.split()
            if int(data[1]) == account_number:
                if int(data[2]) < amount:
                    print("Insufficient balance!")
                    f.write(line)
                else:
                    data[2] = str(int(data[2]) - amount)
                    f.write(' '.join(data) + '\n')
            else:
                f.write(line)

    print("Amount withdrawn successfully!")

def balance_enquiry():
    """
    This function displays the account balance.
    """
    account_number = int(input("Enter your account number: "))

    with open('accounts.txt', 'r') as f:
        for line in f:
            data = line.split()
            if int(data[1]) == account_number:
                print(f"Your account balance is {data[2]}")
                return

    print("Invalid account number!")

def view_details():
    """
    This function displays the account details.
    """
    account_number = int(input("Enter your account number: "))

    with open('accounts.txt', 'r') as f:
        for line in f:
            data = line.split()
            if int(data[1]) == account_number:
                print(f"Name: {data[0]}")
                print(f"Account number: {data[1]}")
                print(f"Balance: {data[2]}")
                return

    print("Invalid account number!")
    
def main():
    while True:
        print("\nWelcome to the banking system!")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password  ")

class Account:
    accounts = {}

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transactions.append(('withdraw', amount))

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

    @classmethod
    def create_account(cls, name, password):
        if name in cls.accounts:
            raise ValueError("Account already exists")
        account = cls(name, password)
        cls.accounts[name] = account
        return account

    @classmethod
    def get_account(cls, name):
        if name not in cls.accounts:
            raise ValueError("Account does not exist")
        return cls.accounts[name]


