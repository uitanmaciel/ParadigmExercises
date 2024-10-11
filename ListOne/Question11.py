# Faça um algoritmo que receba o número de horas trabalhadas e o valor do salário mínimo.
# Calcule e mostre o salário a receber seguindo as regras abaixo:
#
# a)	a hora trabalhada vale a metade do salário mínimo;
# b)	o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
# c)	o imposto equivale a 3% do salário bruto;
# d)	o salário a receber equivale ao salário bruto menos o imposto;

def entry ():
    hours_worked = float(input("Informe o número de horas trabalhadas: "))
    minimum_salary = float(input("Informe o valor do salário mínimo: "))
    return hours_worked, minimum_salary

# Calcula o valor da hora trabalhada
def calculate_hour_value (minimum_salary):
    return minimum_salary / 2

# Calcula o salário bruto
def calculate_gross_salary (hours_worked, hour_value):
    return hours_worked * hour_value

# Calcula o imposto
def calculate_tax (gross_salary):
    return gross_salary * 0.03

# Calcula o salário a receber
def calculate_salary (gross_salary, tax):
    return gross_salary - tax

def main ():
    hours_worked, minimum_salary = entry()
    hour_value = calculate_hour_value(minimum_salary)
    gross_salary = calculate_gross_salary(hours_worked, hour_value)
    tax = calculate_tax(gross_salary)
    salary = calculate_salary(gross_salary, tax)
    print(f"O salário a receber é: R$ {salary:.2f}")