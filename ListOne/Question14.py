# Sabe-se que o quilowatt de energia custa um quinto do salário mínimo.
# Faça um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência.
# Calcule e mostre:
#
# a)	o valor, em reais, de cada quilowatt;
# b)	o valor, em reais, a ser pago por essa residência;
# c)	o valor, em reais, a ser pago com desconto de 15%;

def entry ():
    minimum_salary = float(input("Informe o valor do salário mínimo: "))
    kilowatt = float(input("Informe a quantidade de quilowatts consumida: "))
    return minimum_salary, kilowatt

# Calcula o valor de cada quilowatt
def calculate_kilowatt_value (minimum_salary):
    return minimum_salary / 5

# Calcula o valor a ser pago pela residência
def calculate_value (kilowatt, kilowatt_value):
    return kilowatt * kilowatt_value

# Calcula o desconto de 15%
def calculate_discount (value):
    return value * 0.15

def main ():
    minimum_salary, kilowatt = entry()
    kilowatt_value = calculate_kilowatt_value(minimum_salary)
    value = calculate_value(kilowatt, kilowatt_value)
    discount = calculate_discount(value)
    print(f"O valor de cada quilowatt é: R$ {kilowatt_value:.2f}")
    print(f"O valor a ser pago pela residência é: R$ {value:.2f}")
    print(f"O valor a ser pago com desconto de 15% é: R$ {value - discount:.2f}")