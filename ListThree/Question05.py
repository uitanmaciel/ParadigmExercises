# Faça um algoritmo que receba a idade, a altura e o peso de 25 pessoas. Calcule e mostre:
#
# 1. A quantidade de pessoas com idade superior a 50 anos;
# 2. A média das alturas das pessoas com idade entre 10 e 20 anos;
# 3. A porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.

def entry():
    people = []
    for i in range(25):
        age = int(input(f"Informe a idade da {i}ª pessoa: "))
        height = float(input(f"Informe a altura {i}ª da pessoa: "))
        weight = float(input(f"Informe o peso {i}ª da pessoa: "))
        people.append([age, height, weight])
    return people

def response(people):
    over50 = 0
    height = 0
    weight = 0
    for i in range(25):
        if people[i][0] > 50:
            over50 += 1
        if 10 <= people[i][0] <= 20:
            height += people[i][1]
        if people[i][2] < 40:
            weight += 1
    return over50, height, weight

def main():
    people = entry()
    over50, height, weight = response(people)
    print(f"Quantidade de pessoas com idade superior a 50 anos: {over50}")
    print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {height/15}")
    print(f"Porcentagem de pessoas com peso inferior a 40Kg entre todas as pessoas analisadas: {(weight/25)*100}%")