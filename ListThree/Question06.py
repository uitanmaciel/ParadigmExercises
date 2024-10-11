# Faça um algoritmo que receba a idade e o peso de sete pessoas. Calcule e mostre:
#
# 1. a quantidade de pessoas com mais de 90 quilos;
# 2. a média das idades das sete pessoas.

def entry():
    people = []
    for i in range(7):
        age = int(input(f"Informe a idade da {i+1}ª pessoa: "))
        weight = float(input(f"Informe o peso da {i+1}ª pessoa: "))
        people.append([age, weight])
    return people

def response(people):
    over90 = 0
    age = 0
    for i in range(7):
        if people[i][1] > 90:
            over90 += 1
        age += people[i][0]
    return over90, age

def main():
    people = entry()
    over90, age = response(people)
    print(f"Quantidade de pessoas com mais de 90Kg: {over90}")
    print(f"Média das idades das 7 pessoas: {age/7}")