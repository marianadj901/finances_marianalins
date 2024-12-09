import pytest
from finances.investment import Investment
from finances.account import Account

def test_investment_creation():
    investimento = Investment("Renda Fixa", 1000, 0.01)
    assert investimento.type == "Renda Fixa"
    assert investimento.initial_amount == 1000
    assert investimento.rate_of_return == 0.01

def test_calculate_value():
    # Testando com um investimento de 12 meses
    investimento = Investment("Renda Fixa", 1000, 0.01)
    investimento.date_purchased = investimento.date_purchased.replace(month=1)  # Simula 12 meses
    valor = investimento.calculate_value()
    assert valor > 1000  # Deve ter rendido

    # Testando com um investimento recente (sem rendimento ainda)
    investimento_recente = Investment("Renda Fixa", 1000, 0.01)
    valor_recente = investimento_recente.calculate_value()
    assert valor_recente == 1000  # Ainda não teve rendimento

def test_sell_investment():
    investimento = Investment("Renda Fixa", 1000, 0.01)
    conta = Account("Conta Poupança")
    investimento.sell(conta)
    assert conta.balance > 0
    assert investimento.current_value == 0
