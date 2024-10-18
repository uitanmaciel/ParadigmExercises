def __enunciate():
    print('''# Questão 03 - Faça um algoritmo que receba um número e que calcule e mostre a tabuada desse número.''')

# Calcula a adição de um número
def addition(number):
    for i in range(1, 11):
        if i == 10:
            print(f"{number} + {i} = {number + i}\n")
        else:
            print(f"{number} + {i} = {number + i}")

# Calcula a subtração de um número
def subtraction(number):
    i = number + 1
    count = 0
    for i in range(i, i + 10):
        if count == 9:
            print(f"{i} - {number} = {i - number}\n")
        else:
            print(f"{i} - {number} = {i - number}")
            count += 1

# Calcula a multiplicação de um número
def multiplication(number):
    for i in range(1, 11):
        if i == 10:
            print(f"{number} x {i} = {number * i}\n")
        else:
            print(f"{number} x {i} = {number * i}")

# Calcula a divisão de um número
def division(number):
    count = number
    for i in range(1, 11):
        print(f"{count} / {number} = {count / number}")
        count += number

def main():
    __enunciate()
    print()
    number = int(input("Informe um número: "))
    addition(number)
    subtraction(number)
    multiplication(number)
    division(number)