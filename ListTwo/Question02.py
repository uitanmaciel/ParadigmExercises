# Faça um algoritmo que receba duas notas, calcule e mostre a média aritmética e a mensagem que está na tabela a seguir:
#
#
# | Média Aritmética |	Mensagem  |
# |  0,0         4,0 |  Reprovado |
# |  4,0         7,0 |  Exame     |
# |  7,0        10,0 |  Aprovado  |

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
    if 0 <= average < 4:
        print("Reprovado")
    if 4 <= average < 7:
        print("Exame")
    print("Aprovado")