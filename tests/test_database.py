import os
import tempfile
import json
import unittest
from database import Database, Account, CurrentAccount, SavingsAccount


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.accounts_file = tempfile.NamedTemporaryFile().name
        self.customers_file = tempfile.NamedTemporaryFile().name
        self.db = Database(self.accounts_file, self.customers_file)

    def tearDown(self):
        os.remove(self.accounts_file)
        os.remove(self.customers_file)

    def test_load_accounts(self):
        # Test loading accounts from an empty file
        self.assertEqual(self.db.load_accounts(), {})

        # Test loading accounts from a file with valid data
        accounts_data = {'1': {'account_type': 'savings', 'name': 'John', 'balance': 1000},
                         '2': {'account_type': 'current', 'name': 'Jane', 'balance': 500, 'overdraft': 200}}
        with open(self.accounts_file, 'w') as f:
            json.dump(accounts_data, f)
        expected_accounts = {'1': SavingsAccount('1', 'John', 1000),
                             '2': CurrentAccount('2', 'Jane', 500, 200)}
        self.assertEqual(self.db.load_accounts(), expected_accounts)

        # Test loading accounts from a file with invalid data
        accounts_data = {'1': {'account_type': 'invalid', 'name': 'John', 'balance': 1000}}
        with open(self.accounts_file, 'w') as f:
            json.dump(accounts_data, f)
        self.assertEqual(self.db.load_accounts(), {})

    def test_load_customers(self):
        # Test loading customers from an empty file
        self.assertEqual(self.db.load_customers(), {})

        # Test loading customers from a file with valid data
        customers_data = {'1': {'name': 'John', 'accounts': ['1']},
                          '2': {'name': 'Jane', 'accounts': ['2']}}
        with open(self.customers_file, 'w') as f:
            json.dump(customers_data, f)
        expected_customers = {'1': {'name': 'John', 'accounts': ['1']},
                              '2': {'name': 'Jane', 'accounts': ['2']}}
        self.assertEqual(self.db.load_customers(), expected_customers)

        # Test loading customers from a file with invalid data
        customers_data = {'1': {'name': 'John', 'invalid_key': 'invalid_value'}}
        with open(self.customers_file, 'w') as f:
            json.dump(customers_data, f)
        self.assertEqual(self.db.load_customers(), {})

    def test_save_account(self):
        # Test saving a new account
        account = SavingsAccount('1', 'John', 1000)
        self.db.save_account(account)
        expected_accounts = {'1': account}
        with open(self.accounts_file, 'r') as f:
            self.assertEqual(json.load(f), {'1': {'account_type': 'savings', 'name': 'John', 'balance': 1000}})

        # Test updating an existing account
        account.balance = 2000
        self.db.save_account(account)
        expected_accounts = {'1': account}
        with open(self.accounts_file, 'r') as f:
            self.assertEqual(json.load(f), {'1': {'account_type': 'savings', 'name': 'John', 'balance': 2000}})

    def test_save_customer(self):
        # Test saving a new customer
        customer_id = '1'
        customer_data = {'name': 'John', 'accounts': ['

