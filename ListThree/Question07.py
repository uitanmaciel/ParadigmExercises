# Faça um algoritmo que receba 10 números e que calcule e mostre a quantidade de números entre 30 e 90.

def entry():
    numbers = []
    for i in range(10):
        number = int(input(f"Informe o {i+1}º número: "))
        numbers.append(number)
    return numbers

def response(numbers):
    count = 0
    for i in range(10):
        if 30 <= numbers[i] <= 90:
            count += 1
    return count

def main():
    numbers = entry()
    count = response(numbers)
    print(f"Quantidade de números entre 30 e 90: {count}")