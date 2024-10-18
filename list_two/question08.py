def __enunciate():
    print('''# Questão 08 - Faça um algoritmo que recba o preço de um produto e o seu código de origem e mostre sua procedência.
# A procedência obedece à tabela a seguir.
#
# |--------------------------------------------|
# |    Código de Origem  |	    Procedência    |
# |----------------------|---------------------|
# |           1          |          Sul        |
# |           2          |         Norte       |
# |           3          |         Leste       |
# |           4          |         Oeste       |
# |         5 ou 6       |        Nodeste      |
# |      7 ou 8 ou 9     |        Sudeste      |
# |        10 ou 20      |      Centro-Oste    |
# |         5 ou 6       |        Nodeste      |
# |--------------------------------------------|\n''')

def entry():
    price = float(input('Informe o preço do produto: '))
    origin = int(input('Informe o código de origem do produto: '))
    return price, origin

# Função que retorna a origem do produto
def origin(origin):
    if origin == 1:
        return "Sul"
    if origin == 2:
        return "Norte"
    if origin == 3:
        return "Leste"
    if origin == 4:
        return "Oeste"
    if origin == 5 or origin == 6:
        return "Nordeste"
    if origin == 7 or origin == 8 or origin == 9:
        return "Sudeste"
    if origin == 10 or origin == 20:
        return "Centro-Oeste"
    return "Nodeste"

def main():
    __enunciate()
    price, origin = entry()
    print(f'O produto de preço R${price:.2f} é da região {origin}')