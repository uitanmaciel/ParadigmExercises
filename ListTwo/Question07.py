# Faça um algoritmo que receba a idade de um nadador e mostre sua categoria usando as regras a seguir.
#
# |    Categoria  |	    Idade    |
# |  Infantil     |    5 a 7     |
# |  Juvenil      |    8 a 10    |
# |  Adolescente  |   11 a 15    |
# |  Adulto       |   16 a 30    |
# |  Sênior       |  Acima de 30 |

def entry():
    return int(input('Informe a idade do nadador: '))

# Retorna a categoria do nadador
def category(age):
    if 5 <= age <= 7:
        return "Infantil"
    if 8 <= age <= 10:
        return "Juvenil"
    if 11 <= age <= 15:
        return "Adolescente"
    if 16 <= age <= 30:
        return "Adulto"
    return "Sênior"

def main():
    age = entry()
    print(f'O nadador está na categoria {category(age)}')