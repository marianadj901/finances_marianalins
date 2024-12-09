from datetime import datetime

class Transaction:
    """
    Classe para representar uma transação financeira.

    Atributos:
        amount (float): Valor da transação.
        date (datetime): Data da transação.
        category (str): Categoria da transação.
        description (str): Descrição da transação.
    """
    def __init__(self, amount: float, category: str, description: str = "") -> None:
        """
        Inicializa um objeto Transaction.

        Args:
            amount (float): Valor da transação.
            category (str): Categoria da transação.
            description (str, opcional): Descrição da transação. Padrão é "".
        """
        self.amount: float = amount
        self.date: datetime = datetime.now()
        self.category: str = category
        self.description: str = description

    def __str__(self) -> str:
        """
        Retorna uma descrição da transação no formato:
        'Transação: {description} R${amount:0.2f} ({category})'.

        Returns:
            str: Descrição formatada da transação.
        """
        return f"Transação: {self.description} R${self.amount:0.2f} ({self.category})"

    def update(self, **attributes) -> None:
        """
        Atualiza um ou mais atributos da transação.

        Args:
            attributes (dict): Atributos a serem atualizados.
        """
        for key, value in attributes.items():
            setattr(self, key, value)
