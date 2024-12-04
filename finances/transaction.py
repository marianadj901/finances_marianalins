from datetime import datetime

class Transaction:
    def __init__(self, amount: float, category: str, description: str = "") -> None:
        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.description = description

    def __str__(self) -> str:
        return f"Transação: {self.description} R${self.amount:0.2f} ({self.category})"

    def update(self, **attributes):
        for key, value in attributes.items():
            setattr(self, key, value)
