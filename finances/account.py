from typing import List
from .transaction import Transaction

class Account:
    def __init__(self, name: str) -> None:
        self.name = name
        self.balance = 0.0
        self.transactions = []

    def add_transaction(self, amount: float, category: str, description: str = "") -> Transaction:
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.balance += amount
        return transaction

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, category: str = None) -> List[Transaction]:
        filtered_transactions = self.transactions
        if start_date:
            filtered_transactions = [t for t in filtered_transactions if t.date >= start_date]
        if end_date:
            filtered_transactions = [t for t in filtered_transactions if t.date <= end_date]
        if category:
            filtered_transactions = [t for t in filtered_transactions if t.category == category]
        return filtered_transactions
