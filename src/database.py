import json
from typing import Dict, List, Union
from src.account import Account


class Database:
    def __init__(self, accounts_file: str, customers_file: str):
        self.accounts_file = accounts_file
        self.customers_file = customers_file
        self.accounts = self.load_accounts()
        self.customers = self.load_customers()

    def load_accounts(self) -> Dict[str, Account]:
        try:
            with open(self.accounts_file, 'r') as f:
                accounts_json = json.load(f)
                accounts = {}
                for acc_num, acc_data in accounts_json.items():
                    if acc_data['account_type'] == 'savings':
                        accounts[acc_num] = SavingsAccount(acc_num, acc_data['name'], acc_data['balance'])
                    elif acc_data['account_type'] == 'current':
                        accounts[acc_num] = CurrentAccount(acc_num, acc_data['name'], acc_data['balance'], acc_data['overdraft'])
                return accounts
        except FileNotFoundError:
            return {}

    def load_customers(self) -> Dict[str, Dict[str, Union[str, List[str]]]]:
        try:
            with open(self.customers_file, 'r') as f:
                customers_json = json.load(f)
                return customers_json
        except FileNotFoundError:
            return {}

    def save_account(self, account: Account) -> None:
        self.accounts[account.acc_num] = account
        self.save_accounts()

    def save_accounts(self) -> None:
        accounts_json = {}
        for acc_num, account in self.accounts.items():
            acc_data = {'account_type': account.__class__.__name__.lower(),
                        'name': account.name,
                        'balance': account.balance}
            if isinstance(account, CurrentAccount):
                acc_data['overdraft'] = account.overdraft
            accounts_json[acc_num] = acc_data
        with open(self.accounts_file, 'w') as f:
            json.dump(accounts_json, f)

    def save_customer(self, customer_id: str, customer_data: Dict[str, Union[str, List[str]]]) -> None:
        self.customers[customer_id] = customer_data
        self.save_customers()

    def save_customers(self) -> None:
        with open(self.customers_file, 'w') as f:
            json.dump(self.customers, f)

