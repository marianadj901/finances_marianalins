import pytest
from finances.account import Account
from finances.transaction import Transaction

def test_add_transaction():
    account = Account('Personal')
    transaction = account.add_transaction(100, 'Food', 'Lunch')
    assert transaction.amount == 100
    assert account.balance == 100
    assert len(account.transactions) == 1
