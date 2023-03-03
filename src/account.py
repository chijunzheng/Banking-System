class Account:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return -1

    def balance_enquiry(self):
        return self.balance

    def view_details(self):
        return f"Name: {self.name}\nAccount Number: {self.account_number}\nBalance: {self.balance}"

