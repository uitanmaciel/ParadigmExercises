def __enunciate():
    print('''# Questão 09 -Faça um algoritmo que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir,
# verifique e mostre em qual grupo de risco essa pessoa se encaixa.
#
# |----------------------------------------------------------------------------|
# |        Idade       |	                      Peso                         |
# |--------------------|-------------------------------------------------------|
# |                    |    Até 60   | Entre 60 e 90 (Inclusive) | Acima de 90 |
# |--------------------|-------------|---------------------------|-------------|
# |    Menores de 20   |       9     |             8             |      7      |
# |     De 20 a 50     |       6     |             5             |      4      |
# |    Maiores de 50   |       3     |             2             |      1      |
# |----------------------------------------------------------------------------|\n''')

def entry():
    age = int(input('Informe a idade da pessoa: '))
    weight = float(input('Informe o peso da pessoa: '))
    return age, weight

# Função que retorna o grupo de risco da pessoa
def risk(age, weight):
    if age < 20:
        if weight <= 60:
            return 9
        if 60 < weight <= 90:
            return 8
        return 7
    if 20 <= age <= 50:
        if weight <= 60:
            return 6
        if 60 < weight <= 90:
            return 5
        return 4
    if weight <= 60:
        return 3
    if 60 < weight <= 90:
        return 2
    return 1

def main():
    __enunciate()
    age, weight = entry()
    print(f'A pessoa de {age} anos e {weight}kg está no grupo de risco {risk(age, weight)}')
