from typing import List
from .account import Account
from .investment import Investment

class Client:
    """
    Classe para representar um cliente.

    Atributos:
        name (str): Nome do cliente.
        accounts (List[Account]): Lista de contas do cliente.
        investments (List[Investment]): Lista de investimentos do cliente.
    """
    def __init__(self, name: str) -> None:
        """
        Inicializa um objeto Client.

        Args:
            name (str): Nome do cliente.
        """
        self.name: str = name
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, account_name: str) -> Account:
        """
        Adiciona uma conta ao cliente.

        Args:
            account_name (str): Nome da conta a ser criada.

        Returns:
            Account: A conta criada.
        """
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        """
        Adiciona um investimento ao cliente.

        Args:
            investment (Investment): O investimento a ser adicionado.
        """
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """
        Calcula o patrimônio líquido do cliente, somando o saldo de todas as contas e o valor de todos os investimentos.

        Returns:
            float: O valor total do patrimônio líquido.
        """
        total = sum(account.balance for account in self.accounts)
        total += sum(investment.calculate_value() for investment in self.investments)
        return total
