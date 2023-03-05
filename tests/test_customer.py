import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def test_customer_creation(self):
        customer = Customer("John Doe", "johndoe@example.com", "password", "123")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "johndoe@example.com")
        self.assertEqual(customer.password, "password")
        self.assertEqual(customer.account_number, "123")
        self.assertEqual(customer.balance, 0)

    def test_deposit(self):
        customer = Customer("John Doe", "johndoe@example.com", "password", "123")
        customer.deposit(100)
        self.assertEqual(customer.balance, 100)

    def test_withdraw(self):
        customer = Customer("John Doe", "johndoe@example.com", "password", "123")
        customer.deposit(100)
        customer.withdraw(50)
        self.assertEqual(customer.balance, 50)

    def test_insufficient_balance(self):
        customer = Customer("John Doe", "johndoe@example.com", "password", "123")
        customer.deposit(100)
        customer.withdraw(150)
        self.assertEqual(customer.balance, 100)

    def test_view_balance(self):
        customer = Customer("John Doe", "johndoe@example.com", "password", "123")
        customer.deposit(100)
        self.assertEqual(customer.view_balance(), "Your balance is 100")

    def test_view_details(self):
        customer = Customer("John Doe", "johndoe@example.com", "password", "123")
        details = "Name: John Doe\nEmail: johndoe@example.com\nAccount Number: 123\nBalance: 0"
        self.assertEqual(customer.view_details(), details)

if __name__ == '__main__':
    unittest.main()

