# Faça um algoritmo que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas
# e a mensagem de aprovado ou reprovado, considerando para aprovação média 7.

def entry():
    grades = []
    for i in range(4):
        grades.append(float(input(f'Informe a {i+1}º nota: ')))
    return grades

# Função que calcula a média das notas
def average(grades):
    return sum(grades) / len(grades)

# Função que verifica se o aluno foi aprovado ou reprovado
def approved(average):
    if average >= 7:
        print("Aprovado")
    print("Reprovado")

def main():
    grades = entry()
    average_grade = average(grades)
    print(f'A nota média é {average_grade:.2f} e você está {approved(average_grade)}')