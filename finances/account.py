from typing import List
from .transaction import Transaction
from datetime import datetime

class Account:
    """
    Classe para representar uma conta bancária.

    Atributos:
        name (str): Nome da conta.
        balance (float): Saldo da conta.
        transactions (List[Transaction]): Lista de transações na conta.
    """
    def __init__(self, name: str) -> None:
        """
        Inicializa um objeto Account.

        Args:
            name (str): Nome da conta.
        """
        self.name: str = name
        self.balance: float = 0.0
        self.transactions: List[Transaction] = []

    def add_transaction(self, amount: float, category: str, description: str = "") -> Transaction:
        """
        Adiciona uma transação à conta e atualiza o saldo.

        Args:
            amount (float): O valor da transação (positivo ou negativo).
            category (str): A categoria da transação.
            description (str, opcional): Uma descrição da transação. Padrão é "".

        Returns:
            Transaction: A transação criada.
        """
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.balance += amount
        return transaction

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, category: str = None) -> List[Transaction]:
        """
        Retorna uma lista de transações filtradas por data e/ou categoria.

        Args:
            start_date (datetime, opcional): Data inicial para filtrar as transações.
            end_date (datetime, opcional): Data final para filtrar as transações.
            category (str, opcional): Categoria para filtrar as transações.

        Returns:
            List[Transaction]: Lista de transações filtradas.
        """
        filtered_transactions = self.transactions
        if start_date:
            filtered_transactions = [t for t in filtered_transactions if t.date >= start_date]
        if end_date:
            filtered_transactions = [t for t in filtered_transactions if t.date <= end_date]
        if category:
            filtered_transactions = [t for t in filtered_transactions if t.category == category]
        return filtered_transactions
