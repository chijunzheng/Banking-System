from src.user import User
import os


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        
    def add_account(self):
        account_no = input("Enter account number: ")
        account_holder_name = input("Enter account holder name: ")
        account_type = input("Enter account type: ")
        opening_balance = input("Enter opening balance: ")
        with open(os.path.join(os.getcwd(), 'accounts.txt'), 'a') as f:
            f.write(f"{account_no},{account_holder_name},{account_type},{opening_balance}\n")
        print("Account added successfully!")
        
    def delete_account(self):
        account_no = input("Enter account number to delete: ")
        accounts = self.get_accounts()
        new_accounts = []
        found = False
        for account in accounts:
            if account[0] == account_no:
                found = True
            else:
                new_accounts.append(account)
        if not found:
            print("Account not found!")
            return
        with open(os.path.join(os.getcwd(), 'accounts.txt'), 'w') as f:
            for account in new_accounts:
                f.write(f"{account[0]},{account[1]},{account[2]},{account[3]}\n")
        print("Account deleted successfully!")
        
    def modify_account(self):
        account_no = input("Enter account number to modify: ")
        accounts = self.get_accounts()
        new_accounts = []
        found = False
        for account in accounts:
            if account[0] == account_no:
                found = True
                account_holder_name = input("Enter new account holder name: ")
                account_type = input("Enter new account type: ")
                opening_balance = input("Enter new opening balance: ")
                new_accounts.append((account_no, account_holder_name, account_type, opening_balance))
            else:
                new_accounts.append(account)
        if not found:
            print("Account not found!")
            return
        with open(os.path.join(os.getcwd(), 'accounts.txt'), 'w') as f:
            for account in new_accounts:
                f.write(f"{account[0]},{account[1]},{account[2]},{account[3]}\n")
        print("Account modified successfully!")
        
    def search_account(self):
        account_no = input("Enter account number to search: ")
        accounts = self.get_accounts()
        found = False
        for account in accounts:
            if account[0] == account_no:
                print(f"Account Number: {account[0]}")
                print(f"Account Holder Name: {account[1]}")
                print(f"Account Type: {account[2]}")
                print(f"Opening Balance: {account[3]}")
                found = True
        if not found:
            print("Account not found!")
                
    def get_accounts(self):
        accounts = []
        with open(os.path.join(os.getcwd(), 'accounts.txt'), 'r') as f:
            lines = f.readlines()
            for line in lines:
                account = line.strip().split(',')
                accounts.append(account)
        return accounts

