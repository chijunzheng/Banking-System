class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def get_username(self):
        return self.username

    def set_password(self, new_password):
        self.password = new_password

    def verify_password(self, password):
        return self.password == password

