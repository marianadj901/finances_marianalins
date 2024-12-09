from datetime import datetime
from .account import Account

class Investment:
    """
    Classe para representar um investimento.

    Atributos:
        type (str): Tipo do investimento (e.g., "Renda Fixa").
        initial_amount (float): Valor inicial do investimento.
        date_purchased (datetime): Data de compra do investimento.
        rate_of_return (float): Taxa mensal de retorno do investimento.
        current_value (float): Valor atual do investimento, calculado com base no tempo e taxa de retorno.
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
        Calcula o valor atual do investimento com base na taxa de retorno e o tempo de aplicação.

        Returns:
            float: O valor atual do investimento.
        """
        months = (datetime.now() - self.date_purchased).days // 30
        self.current_value = self.initial_amount * (1 + self.rate_of_return) ** months
        return self.current_value
