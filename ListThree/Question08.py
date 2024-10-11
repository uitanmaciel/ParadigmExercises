# Faça um algoritmo que receba dez números, calcule e mostre a soma dos números pares e a soma dos números primos.

def entry():
    numbers = []
    for i in range(10):
        number = int(input(f"Informe o {i+1}º número: "))
        numbers.append(number)
    return numbers

# Função que verifica se um número é primo
def is_prime(param):
    if param < 2:
        return False
    for i in range(2, param):
        if param % i == 0:
            return False
    return True

def response(numbers):
    sum_even = 0
    sum_prime = 0
    for i in range(10):
        if numbers[i] % 2 == 0:
            sum_even += numbers[i]
        if is_prime(numbers[i]):
            sum_prime += numbers[i]
    return sum_even, sum_prime

def main():
    numbers = entry()
    sum_even, sum_prime = response(numbers)
    print(f"Soma dos números pares: {sum_even}")
    print(f"Soma dos números primos: {sum_prime}")