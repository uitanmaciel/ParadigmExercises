# Faça um algoritmo que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e classificação.
#
# | TABELA 1 - PERCENTUAL DE AUMENTO |
# | Preço                       |  %   |
# | Até R$ 50,00                |  05  |
# | Entre R$ 50,00 e R$ 100,00  |  10  |
# | Acima de R$ 100,00          |  15  |
#
# | TABELA 2 - CLASSIFICAÇÕES |
# | Novo Preço                  | Classificação  |
# | Até R$ 80,00                |     Barato     |
# | Entre R$ 80,00 e R$ 120,00  |     Normal     |
# | Entre R$ 120,00 e R$ 200,00 |      Caro      |
# | Acima de R$ 100,00          |    Muito Caro  |

def entry():
    return float(input('Informe o preço do produto: '))

# Função que calcula o aumento do preço do produto
def increase(price):
    if price <= 50:
        return price * 1.05
    if 50 < price <= 100:
        return price * 1.1
    return price * 1.15

# Função que classifica o preço do produto
def classification(price):
    if price <= 80:
        return "Barato"
    if 80 < price <= 120:
        return "Normal"
    if 120 < price <= 200:
        return "Caro"
    return "Muito Caro"

def main():
    price = entry()
    print(f'O novo preço é R${increase(price):.2f} e a classificação é {classification(increase(price))}')