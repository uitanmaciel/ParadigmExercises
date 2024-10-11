# Faça um algoritmo que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor de aumento e o novo salário.

def entry ():
    salary = float(input("Informe o salário do funcionário: "))
    increase_percentage = float(input("Informe o percentual de aumento do salário: "))
    return salary, increase_percentage

# Função que calcula o valor do aumento e o novo salário do funcionário
def calculate_salary (salary, increase_percentage):
    increase_value = salary * (increase_percentage / 100)
    new_salary = salary + increase_value
    return increase_value, new_salary

def main ():
    salary, increase_percentage = entry()
    increase_value, new_salary = calculate_salary(salary, increase_percentage)
    print(f"O valor do aumento do salário é: R$ {increase_value:.2f}")
    print(f"O novo salário do funcionário é: R$ {new_salary:.2f}")