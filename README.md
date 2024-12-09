# Finances - Mariana Lins

## Descrição

O pacote `finances` é uma ferramenta completa para o gerenciamento de finanças pessoais. Ele oferece suporte para:
- Criação e gerenciamento de transações financeiras.
- Gerenciamento de contas bancárias e cálculo de saldos.
- Investimentos com cálculo de retorno e integração com contas bancárias.
- Geração de relatórios financeiros detalhados.
- Projeções financeiras para avaliação de valor futuro.

## Instalação

Para instalar o pacote e suas dependências, siga estas etapas:

1. Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd finances
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Instale o pacote localmente:
    ```bash
    pip install .
    ```

## Exemplo de Uso

Aqui está um exemplo básico de como utilizar o pacote:

```python
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
