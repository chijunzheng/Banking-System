import os
import tempfile
import unittest
from src.database import Database
from src.account import Account

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.accounts_file = tempfile.NamedTemporaryFile().name
        self.customers_file = tempfile.NamedTemporaryFile().name
        self.database = Database(self.accounts_file, self.customers_file)

    def tearDown(self):
        os.remove(self.accounts_file)
        os.remove(self.customers_file)

    def test_load_accounts(self):
        # create test data
        account1 = SavingsAccount('1', 'Alice', 1000)
        account2 = CurrentAccount('2', 'Bob', 500, 200)
        self.database.save_account(account1)
        self.database.save_account(account2)

        # reload accounts from database
        self.database.accounts = self.database.load_accounts()

        # check if accounts were loaded correctly
        self.assertEqual(len(self.database.accounts), 2)
        self.assertIsInstance(self.database.accounts['1'], SavingsAccount)
        self.assertEqual(self.database.accounts['1'].name, 'Alice')
        self.assertEqual(self.database.accounts['1'].balance, 1000)
        self.assertIsInstance(self.database.accounts['2'], CurrentAccount)
        self.assertEqual(self.database.accounts['2'].name, 'Bob')
        self.assertEqual(self.database.accounts['2'].balance, 500)
        self.assertEqual(self.database.accounts['2'].overdraft, 200)

    def test_save_account(self):
        # create test data
        account1 = SavingsAccount('1', 'Alice', 1000)

        # save account to database
        self.database.save_account(account1)

        # reload accounts from database
        self.database.accounts = self.database.load_accounts()

        # check if account was saved correctly
        self.assertEqual(len(self.database.accounts), 1)
        self.assertIsInstance(self.database.accounts['1'], SavingsAccount)
        self.assertEqual(self.database.accounts['1'].name, 'Alice')
        self.assertEqual(self.database.accounts['1'].balance, 1000)

    def test_load_customers(self):
        # create test data
        customer1 = {'name': 'Alice', 'accounts': ['1']}
        customer2 = {'name': 'Bob', 'accounts': ['2']}
        self.database.save_customer('1', customer1)
        self.database.save_customer('2', customer2)

        # reload customers from database
        self.database.customers = self.database.load_customers()

        # check if customers were loaded correctly
        self.assertEqual(len(self.database.customers), 2)
        self.assertEqual(self.database.customers['1']['name'], 'Alice')
        self.assertEqual(self.database.customers['1']['accounts'], ['1'])
        self.assertEqual(self.database.customers['2']['name'], 'Bob')
        self.assertEqual(self.database.customers['2']['accounts'], ['2'])

    def test_save_customer(self):
        # create test data
        customer1 = {'name': 'Alice', 'accounts': ['1']}

        # save customer to database
        self.database.save_customer('1', customer1)

        # reload customers from database
        self.database.customers = self.database.load_customers()

        # check if customer was saved correctly
        self.assertEqual(len(self.database.customers), 1)
        self.assertEqual(self.database.customers['1']['name'], 'Alice')
        self.assertEqual(self.database.customers['1']['accounts'], ['1'])

