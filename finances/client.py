from typing import List
from .account import Account
from .investment import Investment

class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts = []
        self.investments = []

    def add_account(self, account_name: str) -> Account:
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        total = sum(account.balance for account in self.accounts)
        total += sum(investment.calculate_value() for investment in self.investments)
        return total
