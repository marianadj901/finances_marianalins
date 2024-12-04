import pytest
from finances.transaction import Transaction

def test_transaction_creation():
    transaction = Transaction(100, 'Food', 'Lunch')
    assert transaction.amount == 100
    assert transaction.category == 'Food'
    assert transaction.description == 'Lunch'
    assert isinstance(transaction.date, datetime)

def test_transaction_update():
    transaction = Transaction(100, 'Food', 'Lunch')
    transaction.update(amount=200, description='Dinner')
    assert transaction.amount == 200
    assert transaction.description == 'Dinner'
