# Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário.
# Faça um algoritmo que calcule e mostre:
#
# 1. a média  dos salários do grupo;
# 2. a maior e menor idade do grupo;
# 3. a quantidade de mulheres com salário até R$ 200,00;
# 4. a idade e o sexo da pessoa que possui o menor salário.
#
# Finalize a entrada de dados ao ser digitada uma idade negativa.

def entry():
    people = []
    while True:
        age = int(input("Informe a idade da pessoa ou digite -1 para SAIR: "))
        if age < 0:
            break
        gender = input("Informe o sexo (M/F): ").upper()
        salary = float(input("Informe o salário: "))
        people.append([age,gender,salary])
    return people

# Retorna a média dos salários por grupo
def calculate_average_salary(people):
    average_salary = sum([person[2] for person in people]) / len(people)
    average_salary_man = sum([person[2] for person in people if person[1] == "M"]) / len([person[2] for person in people if person[1] == "M"])
    average_salary_woman = sum([person[2] for person in people if person[1] == "F"]) / len([person[2] for person in people if person[1] == "F"])
    return average_salary_man, average_salary_woman, average_salary

# Retorna a maior e menor idade do grupo
def calculate_max_min_age(people):
    max_man_age = max([person[0] for person in people if person[1] == "M"])
    min_man_age = min([person[0] for person in people if person[1] == "M"])
    max_woman_age = max([person[0] for person in people if person[1] == "F"])
    min_woman_age = min([person[0] for person in people if person[1] == "F"])
    sun_man_age = sum([person[0] for person in people if person[1] == "M"])
    return max_man_age, min_man_age, max_woman_age, min_woman_age, sun_man_age

# Retorna a quantidade de mulheres com salário até R$ 200,00
def calculate_woman_salary_less_than_200(people):
    salary = [person[2] for person in people if person[1] == "F" and person[2] <= 200]
    return len(salary)

# Retorna a idade e o sexo da pessoa com menor salário
def calculate_person_with_lowest_salary(people):
    lowest_salary = min([person[2] for person in people])
    person = [person for person in people if person[2] == lowest_salary]
    return person

def main():
    people = entry()
    average_salary = calculate_average_salary(people)
    max_min_age = calculate_max_min_age(people)
    count_woman_salary_less_than_200 = calculate_woman_salary_less_than_200(people)
    person_with_lowest_salary = calculate_person_with_lowest_salary(people)
    print(f"A média dos salários dos homens é: {average_salary[0]:.2f}")
    print(f"A média dos salários das mulheres é: {average_salary[1]:.2f}")
    print(f"A média dos salários do grupo é: {average_salary[2]:.2f}")
    print(f"A maior idade dos homens é: {max_min_age[0]}")
    print(f"A menor idade dos homens é: {max_min_age[1]}")
    print(f"A maior idade das mulheres é: {max_min_age[2]}")
    print(f"A menor idade das mulheres é: {max_min_age[3]}")
    print(f"A quantidade de mulheres com salário até R$ 200,00 é: {count_woman_salary_less_than_200}")
    print(f"A pessoa com menor salário tem {person_with_lowest_salary[0][0]} anos e é do sexo {person_with_lowest_salary[0][1]}")