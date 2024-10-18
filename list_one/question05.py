def __enunciate():
    print('''# Questão 05 - Faça um algoritmo que receba o salário-base de um funcionário, calcule e mostre o salário a receber, 
# sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga o 
# imposto de 7% sobre o salário-base.''')

def entry ():
    base_salary = float(input("Informe o salário-base do funcionário: "))
    return base_salary

# Calcula o bônus do funcionário
def calculate_bonus (base_salary):
    bonus = base_salary * 0.05
    return bonus

# Calcula o imposto do funcionário
def calculate_tax (base_salary):
    tax = base_salary * 0.07
    return tax

# Calcula o salário a receber do funcionário
def calculate_salary (base_salary, bonus, tax):
    return base_salary + bonus - tax

def main ():
    __enunciate()
    print()
    base_salary = entry()
    bonus = calculate_bonus(base_salary)
    tax = calculate_tax(base_salary)
    salary = calculate_salary(base_salary, bonus, tax)
    print(f"O salário a receber do funcionário é: R$ {salary:.2f}")
