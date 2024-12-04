from finances import Client, generate_report, future_value_report
from datetime import datetime

# Criando um cliente
cliente = Client("Maria Lins")

# Adicionando uma conta ao cliente
conta = cliente.add_account("Conta Corrente")
conta.add_transaction(2000, "Salário", "Recebimento de salário")
conta.add_transaction(-500, "Alimentação", "Compra no supermercado")
conta.add_transaction(-200, "Transporte", "Combustível")

# Adicionando um investimento
from finances.investment import Investment
investimento = Investment("Renda Fixa", 5000, 0.01)  # 1% ao mês
cliente.add_investment(investimento)

# Gerando relatórios
print(generate_report(cliente))
print(future_value_report(cliente, datetime(2025, 12, 31)))
