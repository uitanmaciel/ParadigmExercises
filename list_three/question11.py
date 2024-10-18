def __enunciate():
    print('''# Questão 11 - A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos.
# A prefeitura deseja saber:
#
# 1. a média do salário da população;
# 2. a média do número de filhos;
# 3. o maior salário;
# 4. a percentagem de pessoas com salários até R$ 150,00.
#
# O final da leitura dos dados dar-se-á com a entrada de um salário negativo.\n''')

def entry():
    people = []
    while True:
        salary = float(input("Informe o salário: "))
        if salary < 0:
            break
        children = int(input("Informe o número de filhos: "))
        people.append([salary, children])
    return people

def response(people):
    salary = 0
    children = 0
    greater_salary = 0
    salary_150 = 0
    for i in range(len(people)):
        salary += people[i][0]
        children += people[i][1]
        if people[i][0] > greater_salary:
            greater_salary = people[i][0]
        if people[i][0] <= 150:
            salary_150 += 1
    return salary/len(people), children/len(people), greater_salary, (salary_150/len(people))*100

def main():
    __enunciate()
    people = entry()
    average_salary, average_children, greater_salary, percentage_salary_150 = response(people)
    print(f"Média do salário da população: {average_salary}")
    print(f"Média do número de filhos: {average_children}")
    print(f"Maior salário: {greater_salary}")
    print(f"Porcentagem de pessoas com salários até R$ 150,00: {percentage_salary_150}%")