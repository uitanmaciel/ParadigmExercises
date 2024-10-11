# Faça um algoritmo que receba a idade e opeso de 15 pessoas. Calcule e mostre as médias dos pesos das pessoas da mesma
# faixa etária. As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e maiores de 31 anos.

def entry():
    people = []
    for i in range(15):
        age = int(input(f"Informe a idade da {i+1}ª pessoa: "))
        weight = float(input(f"Informe o peso da {i+1}ª pessoa: "))
        people.append([age, weight])
    return people

def response(people):
    age1to10 = 0
    age11to20 = 0
    age21to30 = 0
    age31more = 0
    weight1to10 = 0
    weight11to20 = 0
    weight21to30 = 0
    weight31more = 0
    for i in range(15):
        if 1 <= people[i][0] <= 10:
            age1to10 += 1
            weight1to10 += people[i][1]
        elif 11 <= people[i][0] <= 20:
            age11to20 += 1
            weight11to20 += people[i][1]
        elif 21 <= people[i][0] <= 30:
            age21to30 += 1
            weight21to30 += people[i][1]
        else:
            age31more += 1
            weight31more += people[i][1]
    return weight1to10/age1to10, weight11to20/age11to20, weight21to30/age21to30, weight31more/age31more

def main():
    people = entry()
    weight1to10, weight11to20, weight21to30, weight31more = response(people)
    print(f"Média dos pesos das pessoas de 1 a 10 anos: {weight1to10}")
    print(f"Média dos pesos das pessoas de 11 a 20 anos: {weight11to20}")
    print(f"Média dos pesos das pessoas de 21 a 30 anos: {weight21to30}")
    print(f"Média dos pesos das pessoas com mais de 31 anos: {weight31more}")