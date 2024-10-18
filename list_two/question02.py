def __enunciate():
    print('''# Questão 02 - Faça um algoritmo que receba duas notas, calcule e mostre a média aritmética e a mensagem que está na tabela a seguir:
#
#
# | Média Aritmética |	Mensagem  |
# |------------------|------------|
# |  0,0         4,0 |  Reprovado |
# |  4,0         7,0 |  Exame     |
# |  7,0        10,0 |  Aprovado  |\n''')

def entry():
    grades = []
    for i in range(2):
        grades.append(float(input(f'Informe a {i+1}º nota: ')))
    return grades

# Função que calcula a média aritmética
def average(grades):
    return sum(grades) / len(grades)

# Função que verifica a média e imprime a mensagem
def approved(average):
    if 0 <= average <= 4.99:
        return "Reprovado"
    elif 5 <= average <= 6.99:
        return "Exame"
    else:
        return "Aprovado"

def main():
    __enunciate()
    grades = entry()
    average_grade = average(grades)
    print(f'Média: {average_grade}')
    print(f"Situação do Aluno: {approved(average_grade)}")    