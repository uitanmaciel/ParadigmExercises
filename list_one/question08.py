def __enunciate():
    print('''# Questão 08 - Faça um algoritmo que receba um número positivo e maior que zero, calcule e mostre:
#
# a)	o número digitado ao quadrado;
# b)	o número digitado ao cubo;
# c)	a raiz quadrada do número digitado;
# d)	a raiz cúbica do número digitado;''')

def entry ():
    while True:
        number = float(input("Informe um número positivo e maior que zero: "))
        if number > 0:
            return number
        else:
            print("Número inválido. Tente novamente.")

# Calcula o quadrado do número
def calculate_square (number):
    return number ** 2

# Calcula o cubo do número
def calculate_cube (number):
    return number ** 3

# Calcula a raiz quadrada do número
def calculate_square_root (number):
    return number ** 0.5

# Calcula a raiz cúbica do número
def calculate_cube_root (number):
    return number ** (1/3)

def main ():
    __enunciate()
    print()
    number = entry()
    square = calculate_square(number)
    cube = calculate_cube(number)
    square_root = calculate_square_root(number)
    cube_root = calculate_cube_root(number)
    print(f"O número digitado ao quadrado é: {square:.2f}")
    print(f"O número digitado ao cubo é: {cube:.2f}")
    print(f"A raiz quadrada do número digitado é: {square_root:.2f}")
    print(f"A raiz cúbica do número digitado é: {cube_root:.2f}")