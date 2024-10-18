def _enunciate():
    print('''# Questão 05 - Um banco concederá um crédito especial aos seus clientes de acordo com o saldo médio no último ano.
# Faça um algoritmo que receba o saldo médio de um cliente e calcule o valor do crédito, # de acordo com a tabela a seguir.
# Mostre o saldo médio e o valor do crédito.
#
# |---------------------------------------------------|
# |       Saldo Médio           |	   Percentual     |
# |---------------------------- |---------------------|
# |  Acima de R$ 400,00         |  30% do saldo médio |
# |  R$ 400,00        R$ 300,00 |  25% do saldo médio |
# |  R$ 300,00        R$ 200,00 |  20% do saldo médio |
# |  Até R$ 200,00              |  20% do saldo médio |
# |---------------------------------------------------|\n''')

def entry():
    return float(input('Informe o saldo médio do cliente: '))

# Calcula o crédito de acordo com a tabela
def credit(salary):
    if salary > 400:
        return salary * 0.3
    if 300 <= salary <= 400:
        return salary * 0.25
    if 200 <= salary < 300:
        return salary * 0.2
    return salary * 0.2

def main():
    _enunciate()
    salary = entry()
    print(f'O saldo médio é R${salary:.2f} e o valor do crédito é R${credit(salary):.2f}')