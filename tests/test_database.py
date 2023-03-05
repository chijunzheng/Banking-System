import os
import tempfile
import unittest
from src.account import Account, CurrentAccount, SavingsAccount
from src.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Create temporary files for testing
        self.accounts_file = tempfile.NamedTemporaryFile(delete=False).name
        self.customers_file = tempfile.NamedTemporaryFile(delete=False).name

        # Create database object
        self.db = Database(self.accounts_file, self.customers_file)

    def tearDown(self):
        # Delete temporary files after testing
        os.remove(self.accounts_file)
        os.remove(self.customers_file)

    def test_load_accounts(self):
        # Test loading accounts from empty file
        self.db.save_accounts()
        self.db.accounts = self.db.load_accounts()
        self.assertEqual(len(self.db.accounts), 0)

        # Test loading accounts from non-empty file
        acc1 = SavingsAccount("123", "John Doe", 1000)
        self.db.save_account(acc1)
        self.db.accounts = self.db.load_accounts()
        self.assertEqual(len(self.db.accounts), 1)
        self.assertEqual(self.db.accounts["123"].name, "John Doe")
        self.assertEqual(self.db.accounts["123"].balance, 1000)

        # Test loading accounts from file with invalid data
        with open(self.accounts_file, "w") as f:
            f.write("invalid data")
        self.db.accounts = self.db.load_accounts()
        self.assertEqual(len(self.db.accounts), 0)

    def test_load_customers(self):
        # Test loading customers from empty file
        self.db.save_customers()
        self.db.customers = self.db.load_customers()
        self.assertEqual(len(self.db.customers), 0)

        # Test loading customers from non-empty file
        customer_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "accounts": ["123"]
        }
        self.db.save_customer("1", customer_data)
        self.db.customers = self.db.load_customers()
        self.assertEqual(len(self.db.customers), 1)
        self.assertEqual(self.db.customers["1"]["name"], "John Doe")
        self.assertEqual(self.db.customers["1"]["email"], "johndoe@example.com")
        self.assertEqual(self.db.customers["1"]["accounts"], ["123"])

        # Test loading customers from file with invalid data
        with open(self.customers_file, "w") as f:
            f.write("invalid data")
        self.db.customers = self.db.load_customers()
        self.assertEqual(len(self.db.customers), 0)

    def test_save_account(self):
        # Test saving account to empty file
        acc1 = SavingsAccount("123", "John Doe", 1000)
        self.db.save_account(acc1)
        with open(self.accounts_file, "r") as f:
            accounts_json = f.read()
        expected_json = '{"123": {"account_type": "savings", "name": "John Doe", "balance": 1000}}'
        self.assertEqual(accounts_json.strip(), expected_json)

        # Test saving account to non-empty file
        acc2 = CurrentAccount("456", "Jane Doe", 500, 1000)
        self.db.save_account(acc2)
        with open(self.accounts_file, "r") as f:
            accounts_json = f.read()
        expected_json = '{"123": {"account_type": "savings", "name": "John Doe", "balance": 1000}, "456": {"account_type": "current", "name": "Jane Doe", "balance": 500, "

