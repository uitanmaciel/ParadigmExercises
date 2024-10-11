# Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
#
# a)	a idade desa pessoa;
# b)	quantos anos essa pessoa terá em 2030;

def entry ():
    birth_year = int(input("Informe o ano de nascimento da pessoa: "))
    current_year = int(input("Informe o ano atual: "))
    return birth_year, current_year

# Função que calcula a idade da pessoa
def calculate_age (birth_year, current_year):
    return current_year - birth_year

# Função que calcula a idade da pessoa em 2030
def calculate_future_age (age):
    return age + 2030

def main ():
    birth_year, current_year = entry()
    age = calculate_age(birth_year, current_year)
    future_age = calculate_future_age(age)
    print(f"A idade da pessoa é: {age} anos")
    print(f"A pessoa terá {future_age} anos em 2030")