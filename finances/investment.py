from datetime import datetime
from .account import Account

class Investment:
    """
    Classe para representar um investimento.

    Atributos:
        type (str): Tipo do investimento.
        initial_amount (float): Valor inicial do investimento.
        date_purchased (datetime): Data da compra do investimento.
        rate_of_return (float): Taxa mensal de retorno.
        current_value (float): Valor atual do investimento.
    """
    def __init__(self, type: str, initial_amount: float, rate_of_return: float) -> None:
        """
        Inicializa um objeto Investment.

        Args:
            type (str): Tipo do investimento.
            initial_amount (float): Valor inicial do investimento.
            rate_of_return (float): Taxa mensal de retorno.
        """
        self.type: str = type
        self.initial_amount: float = initial_amount
        self.date_purchased: datetime = datetime.now()
        self.rate_of_return: float = rate_of_return
        self.current_value: float = initial_amount

    def calculate_value(self) -> float:
        """
        Calcula o valor atual do investimento, considerando o tempo de aplicação.

        Returns:
            float: Valor atual do investimento.
        """
        months = (datetime.now() - self.date_purchased).days // 30
        self.current_value = self.initial_amount * (1 + self.rate_of_return) ** months
        return self.current_value

    def sell(self, account: Account) -> None:
        """
        Vende o investimento e adiciona o valor à conta do cliente.

        Args:
            account (Account): A conta onde o valor será depositado.
        """
        account.add_transaction(self.current_value, 'Investment Sale', f'Sale of {self.type} investment')
        self.current_value = 0
