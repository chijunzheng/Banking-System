import unittest
from ..src/customer import Customer


class TestCustomer(unittest.TestCase):

    def test_customer_creation(self):
        customer = Customer('John', 'Doe', 'johndoe@example.com', 'password')
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.last_name, 'Doe')
        self.assertEqual(customer.email, 'johndoe@example.com')
        self.assertEqual(customer.password, 'password')

    def test_customer_deposit(self):
        customer = Customer('John', 'Doe', 'johndoe@example.com', 'password')
        customer.deposit(100)
        self.assertEqual(customer.balance, 100)

    def test_customer_withdraw(self):
        customer = Customer('John', 'Doe', 'johndoe@example.com', 'password')
        customer.deposit(100)
        customer.withdraw(50)
        self.assertEqual(customer.balance, 50)

    def test_customer_insufficient_funds(self):
        customer = Customer('John', 'Doe', 'johndoe@example.com', 'password')
        with self.assertRaises(ValueError):
            customer.withdraw(50)

if __name__ == '__main__':
    unittest.main()

