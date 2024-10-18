def __enunciate():
    print('''# Questão 12 - Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária. Esse trabalhador emitiu
# dois cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga CPMF de 0,38%
# e o saldo inicial da conta está zerado.''')

def entry ():
    salary = float(input("Informe o salário recebido: "))
    cheque1 = float(input("Informe o valor do primeiro cheque: "))
    cheque2 = float(input("Informe o valor do segundo cheque: "))
    return salary, cheque1, cheque2

# Calcula o valor do CPMF
def calculate_cpmf (value):
    return value * 0.0038

# Calcula o saldo atual
def calculate_balance (salary, cheque1, cheque2):
    return salary - cheque1 - cheque2 - calculate_cpmf(cheque1) - calculate_cpmf(cheque2)

def main ():
    __enunciate()
    print()
    salary, cheque1, cheque2 = entry()
    print(f"\nO saldo inicial é: R$ 0,00")
    print(f"Depósito de Salário:                                R$ {salary:.2f}")
    print(f"Saldo atual:                                        R$ {salary:.2f}")
    print(f"Cheque a compensar:                                 -R$ {cheque1:.2f}")
    print(f"Cheque a compensar:                                 -R$ {cheque2:.2f}")
    print(f"CPMF sobre os cheque:                              -R$ {calculate_cpmf(cheque1)+calculate_cpmf(cheque2):.2f}")
    balance = calculate_balance(salary, cheque1, cheque2)
    print(f"O saldo atual é:                                    R$ {balance:.2f}")