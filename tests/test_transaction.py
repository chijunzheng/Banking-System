import transaction
import account
import customer
import admin
import pytest

@pytest.fixture
def create_customer():
    customer = Customer("John", "Doe", "johndoe@example.com")
    account = Account(customer)
    return customer, account

@pytest.fixture
def create_admin():
    admin = Admin("Jane", "Doe", "janedoe@example.com")
    return admin

@pytest.fixture
def create_transaction(create_customer, create_admin):
    customer, account = create_customer
    admin = create_admin
    transaction = Transaction("deposit", 100, account, customer, admin)
    return transaction

def test_transaction_amount(create_transaction):
    transaction = create_transaction
    assert transaction.amount == 100

def test_transaction_type(create_transaction):
    transaction = create_transaction
    assert transaction.type == "deposit"

def test_transaction_account(create_transaction, create_customer):
    transaction = create_transaction
    customer, account = create_customer
    assert transaction.account == account

def test_transaction_customer(create_transaction, create_customer):
    transaction = create_transaction
    customer, account = create_customer
    assert transaction.customer == customer

def test_transaction_admin(create_transaction, create_admin):
    transaction = create_transaction
    admin = create_admin
    assert transaction.admin == admin

