# Uma loja utiliza o código “V” para transação à vista e “P” para transação à prazo. Faça um algoritmo que receba o código e o valor de 15 transações. Calcule e mostre:
#
# 1. o valor total das compras à vista;
# 2. o valor total das compras a prazo;
# 3. o valor total das compras efetuadas;
# 4. o valor da primeira prestação das compras a prazo, sabendo-se que essas serão pagas em três vezes.

def entry():
    transactions = []
    while True:
        code = input("Informe o código da transação (V para à vista, P para à prazo ou S para terminar a lista): \n")
        if code == "S":
            break
        value = float(input("Informe o valor da transação: "))
        transactions.append((code, value))
    return transactions

# Calcula o valor total das transações
def total_value(transactions):
    total = 0
    for transaction in transactions:
        total += transaction[1]
    return total

# Calcula o valor total das transações à vista
def total_value_cash(transactions):
    total = 0
    for transaction in transactions:
        if transaction[0] == "V":
            total += transaction[1]
    return total

# Calcula o valor total das transações à prazo
def total_value_installments(transactions):
    total = 0
    for transaction in transactions:
        if transaction[0] == "P":
            total += transaction[1]
    return total

# Calcula o valor da primeira prestação das compras à prazo
def first_installment(transactions):
    total = total_value_installments(transactions) / 3
    return total

def main():
    transactions = entry()
    print(f"Valor total das compras à vista: R$ {total_value_cash(transactions):.2f}")
    print(f"Valor total das compras à prazo: R$ {total_value_installments(transactions):.2f}")
    print(f"Valor total das compras efetuadas: R$ {total_value(transactions):.2f}")
    print(f"Valor da primeira prestação das compras a prazo: R$ {first_installment(transactions):.2f}")