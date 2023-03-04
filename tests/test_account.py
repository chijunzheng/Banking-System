import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("Alice", 1000, "123456")

    def test_deposit(self):
        self.assertEqual(self.account.deposit(500), 1500)
        self.assertEqual(self.account.deposit(-500), 1500)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(500), 500)
        self.assertEqual(self.account.withdraw(-500), -1)
        self.assertEqual(self.account.withdraw(1500), -1)

    def test_balance_enquiry(self):
        self.assertEqual(self.account.balance_enquiry(), 1000)

    def test_view_details(self):
        expected_output = "Name: Alice\nAccount Number: 123456\nBalance: 1000"
        self.assertEqual(self.account.view_details(), expected_output)

if __name__ == '__main__':
    unittest.main()

