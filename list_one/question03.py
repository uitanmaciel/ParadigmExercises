def __enunciate():
    print('''# Questão 03 - Faça um algoritmo que receba o salário de um funcionário, calcule e mostre o novo salário,
# sabendo-se que este sofreu um aumento de 25%.''')

def entry ():
    salary = float(input("Informe o salário do funcionário: "))
    return salary

# Calcula o novo salário com 25% de aumento
def calculate_salary (salary):
    return salary * 1.25

def main ():
    __enunciate()
    print()
    salary = entry()
    new_salary = calculate_salary(salary)
    print(f"O novo salário do funcionário é: R$ {new_salary:.2f}")