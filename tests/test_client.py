import pytest
from finances.client import Client
from finances.account import Account
from finances.investment import Investment

def test_client_creation():
    cliente = Client("João")
    assert cliente.name == "João"
    assert cliente.accounts == []
    assert cliente.investments == []

def test_add_account():
    cliente = Client("João")
    conta = cliente.add_account("Conta Poupança")
    assert isinstance(conta, Account)
    assert conta.name == "Conta Poupança"
    assert conta in cliente.accounts

def test_add_investment():
    cliente = Client("João")
    investimento = Investment("Renda Fixa", 1000, 0.02)
    cliente.add_investment(investimento)
    assert investimento in cliente.investments

def test_net_worth():
    cliente = Client("João")
    conta = cliente.add_account("Conta Corrente")
    conta.add_transaction(1000, "Salário", "Pagamento")
    investimento = Investment("Renda Fixa", 2000, 0.01)
    cliente.add_investment(investimento)
    assert cliente.get_net_worth() > 3000  # Considera o rendimento do investimento
