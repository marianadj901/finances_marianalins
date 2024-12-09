from datetime import datetime
from .account import Account
from .investment import Investment

def generate_report(client) -> str:
    """
    Gera um relatório financeiro detalhado para um cliente.

    Args:
        client (Client): O cliente para o qual o relatório será gerado.

    Returns:
        str: Relatório financeiro formatado.
    """
    report = f"Relatório Financeiro de {client.name}\n"
    report += "=" * 50 + "\n\n"

    # Relatório de Contas
    report += "Contas:\n"
    for account in client.accounts:
        report += f"- {account.name}\n"
        report += f"  Saldo: R$ {account.balance:0.2f}\n"
        report += "  Transações:\n"
        for transaction in account.transactions:
            report += f"    - {transaction}\n"
        report += "\n"

    # Relatório de Investimentos
    report += "Investimentos:\n"
    for investment in client.investments:
        report += f"- {investment.type}\n"
        report += f"  Valor inicial: R$ {investment.initial_amount:0.2f}\n"
        report += f"  Valor atual: R$ {investment.calculate_value():0.2f}\n"
        report += f"  Rendimento mensal: {investment.rate_of_return * 100}%\n"
        report += "\n"

    # Patrimônio líquido
    net_worth = client.get_net_worth()
    report += f"Patrimônio líquido: R$ {net_worth:0.2f}\n"

    return report


def future_value_report(client, date: datetime) -> str:
    if not client.investments:
        return "Nenhum investimento encontrado para projeção."

    report = f"Relatório de Projeção de Rendimentos Futuros - {client.name}\n"
    report += "=" * 50 + "\n\n"

    # Projeção de valor futuro dos investimentos
    report += "Investimentos:\n"
    for investment in client.investments:
        months_to_project = (date.year - investment.date_purchased.year) * 12 + (date.month - investment.date_purchased.month)
        projected_value = investment.initial_amount * (1 + investment.rate_of_return) ** months_to_project
        report += f"- {investment.type}\n"
        report += f"  Valor projetado para {date.strftime('%d/%m/%Y')}: R$ {projected_value:0.2f}\n"
        report += "\n"

    # Projeção de patrimônio líquido
    projected_net_worth = client.get_net_worth()  # Assume que o patrimônio líquido será igual para a projeção
    report += f"Patrimônio líquido projetado para {date.strftime('%d/%m/%Y')}: R$ {projected_net_worth:0.2f}\n"

    return report
