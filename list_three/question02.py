def __enunciate():
    print('''# Questão 02 - Faça um algoritmo que receba a idade de dez pessoas e que calcule e mostre a 
# quantidade de pessoas com idade maior ou igual a 18 anos.''')

def main():
    __enunciate()
    print()
    count = 0
    for i in range(10):
        age = int(input(f"Informe a idade da {i + 1}ª pessoa: "))
        if age >= 18:
            count += 1
    print(f"Número de pessoas com 18 anos ou mais: {count}")