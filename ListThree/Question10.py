# Faça um algoritmo que receba várias idades e que calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.

def entry():
    ages = []
    while True:
        age = int(input("Informe a idade: "))
        if age == 0:
            break
        ages.append(age)
    return ages

def response(ages):
    sum_ages = 0
    for i in range(len(ages)):
        sum_ages += ages[i]
    return sum_ages/len(ages)

def main():
    ages = entry()
    average = response(ages)
    print(f"Média das idades: {average}")