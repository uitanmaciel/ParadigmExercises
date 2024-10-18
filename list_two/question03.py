def __enunciate():
    print('''# Questão 03 - Faça um algoritmo que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário.
#
# |-----------------------------------------------------|
# | Escolha |	            Operação                    |
# |---------|-------------------------------------------|
# |    1    |  Média entre os números digitados         |
# |    2    |  Diferença do maior número pelo menor     |
# |    3    |  Produto entre os números digitados       |
# |    4    |  Divisão do primeiro número pelo segundo  |
# |-----------------------------------------------------|\n''')

def entry():
    numbers = []
    for i in range(2):
        numbers.append(float(input(f'Informe o {i+1}º número: ')))
    return numbers

# Calcula a média entre os números digitados
def average(numbers):
    return sum(numbers) / len(numbers)

# Calcula a diferença do maior número pelo menor
def difference(numbers):
    return max(numbers) - min(numbers)

# Calcula o produto entre os números digitados
def product(numbers):
    return numbers[0] * numbers[1]

# Calcula a divisão do primeiro número pelo segundo
def division(numbers):
    return numbers[0] / numbers[1]

def main():
    __enunciate()
    numbers = entry()
    choice = int(input('Escolha uma operação:\n1 - Média entre os números digitados\n2 - Diferença do maior número pelo menor\n3 - Produto entre os números\n4 - Divisão do primeiro número pelo segundo\n'))
    if choice == 1:
        print(f'A média entre os números digitados é {average(numbers):.2f}')
    if choice == 2:
        print(f'A diferença do maior número pelo menor é {difference(numbers):.2f}')
    if choice == 3:
        print(f'O produto entre os números digitados é {product(numbers):.2f}')
    if choice == 4:
        print(f'A divisão do primeiro número pelo segundo é {division(numbers):.2f}')