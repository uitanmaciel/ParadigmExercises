# 15.	Faça um algoritmo que receba um conjunto de valores inteiros e positivos e que calcule e mostre o maior e o menor valor do conjunto. Considere que:
#
# 1. para encerrar a entrada de dados, deve ser digitado o valor zero;
# 2. para valores negativos, deve ser enviada uma mensagem;
# 3. os valores negativos ou iguais a zero não entrarão nos cálculos.

def entry():
    numbers = []
    while True:
        number = int(input("Informe um número inteiro maior que 0 (ZERO) ou 0 (ZERO) para SAIR: "))
        if number < 0:
            print("Números negativos não são permitidos.")
        elif number == 0:
            break
        else:
            numbers.append(number)
    return numbers

def main():
    numbers = entry()
    if len(numbers) == 0:
        print("Nenhum número informado.")
    else:
        print(f"O maior número informado foi: {max(numbers)}")
        print(f"O menor número informado foi: {min(numbers)}")