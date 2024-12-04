from datetime import datetime
from .account import Account

class Investment:
    def __init__(self, type: str, initial_amount: float, rate_of_return: float) -> None:
        self.type = type
        self.initial_amount = initial_amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return
        self.current_value = initial_amount

    def calculate_value(self) -> float:
        months = (datetime.now() - self.date_purchased).days // 30
        self.current_value = self.initial_amount * (1 + self.rate_of_return) ** months
        return self.current_value

    def sell(self, account: Account) -> None:
        account.add_transaction(self.current_value, 'Investment Sale', f'Sale of {self.type} investment')
        self.current_value = 0
