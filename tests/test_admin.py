import pytest
from banking_system.admin import Admin


class TestAdmin:
    def test_create_account(self):
        admin = Admin("John", "Doe", "john@doe.com", "password")
        account = admin.create_account("Alice", "Smith", "alice@smith.com", "password")
        assert account.first_name == "Alice"
        assert account.last_name == "Smith"
        assert account.email == "alice@smith.com"
        assert account.check_password("password")

    def test_delete_account(self):
        admin = Admin("John", "Doe", "john@doe.com", "password")
        account = admin.create_account("Alice", "Smith", "alice@smith.com", "password")
        admin.delete_account(account)
        assert account not in admin.accounts

    def test_view_accounts(self):
        admin = Admin("John", "Doe", "john@doe.com", "password")
        account1 = admin.create_account("Alice", "Smith", "alice@smith.com", "password")
        account2 = admin.create_account("Bob", "Jones", "bob@jones.com", "password")
        accounts = admin.view_accounts()
        assert len(accounts) == 2
        assert account1 in accounts
        assert account2 in accounts

    def test_reset_password(self):
        admin = Admin("John", "Doe", "john@doe.com", "password")
        account = admin.create_account("Alice", "Smith", "alice@smith.com", "password")
        admin.reset_password(account, "new_password")
        assert account.check_password("new_password")

    def test_update_account(self):
        admin = Admin("John", "Doe", "john@doe.com", "password")
        account = admin.create_account("Alice", "Smith", "alice@smith.com", "password")
        admin.update_account(account, first_name="Alison", last_name="Smyth", email="alison@smyth.com")
        assert account.first_name == "Alison"
        assert account.last_name == "Smyth"
        assert account.email == "alison@smyth.com"

