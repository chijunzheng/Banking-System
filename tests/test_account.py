import pytest
from account import Account

def test_account_creation():
    acc = Account("John Doe", 500)
    assert acc.owner == "John Doe"
    assert acc.balance == 500

def test_deposit():
    acc = Account("John Doe", 500)
    acc.deposit(100)
    assert acc.balance == 600

def test_withdraw():
    acc = Account("John Doe", 500)
    acc.withdraw(200)
    assert acc.balance == 300

def test_insufficient_balance():
    acc = Account("John Doe", 500)
    with pytest.raises(ValueError):
        acc.withdraw(600)

