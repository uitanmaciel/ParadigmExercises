def __enunciate():
    print('''# Questão 07 - Faça um algoritmo que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre
# o valor do rendimento e o valor total depois do rendimento.''')

def entry ():
    deposit = float(input("Informe o valor do depósito: "))
    interest_rate = float(input("Informe o valor da taxa de juros: "))
    return deposit, interest_rate

# Calcula o rendimento
def calculate_interest (deposit, interest_rate):
    interest = deposit * (interest_rate / 100)
    return interest

# Calcula o total
def calculate_total (deposit, interest):
    return deposit + interest

def main ():
    __enunciate()
    print()
    deposit, interest_rate = entry()
    interest = calculate_interest(deposit, interest_rate)
    total = calculate_total(deposit, interest)
    print(f"O valor do rendimento é: R$ {interest:.2f}")
    print(f"O valor total depois do rendimento é: R$ {total:.2f}")