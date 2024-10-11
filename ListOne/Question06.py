# Faça um algoritmo que receba o salário-base de um funcionário, calcule e mostre o seu salário a receber,
# sabendo-se que esse funcionário tem gratificação de R$ 50,00 e paga imposto de 10% sobre o salário-base.

def entry ():
    base_salary = float(input("Informe o salário-base do funcionário: "))
    return base_salary

# Retorna o valor do bonus
def calculate_bonus (bonus):
    return bonus

# Calcula o valor do imposto
def calculate_tax (base_salary):
    return base_salary * 0.10

# Calcula o salário a receber
def calculate_salary (base_salary, bonus, tax):
    return base_salary + bonus - tax

def main ():
    base_salary = entry()
    bonus = calculate_tax(50)
    tax = calculate_tax(base_salary)
    salary = calculate_salary(base_salary, bonus, tax)
    print(f"O salário a receber do funcionário é: R$ {salary:.2f}")