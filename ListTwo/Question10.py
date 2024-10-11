# Faça um algoritmo que receba:
#
# a) o código do produto comprado;
# b) a quantidade comprada de um produto;
#
# Calcule e mostre:
#
# 1. o preço unitário do produto comprado segundo a Tabela I;
# 2. o preço total da nota;
# 3. o valor do desconto, segundo a Tabela II e aplicado sobre o preço total da nota;
# 4. o preço final da nota depois do desconto.
#
# |                   TABELA 1                    |
# | Código do Produto    |          Preço         |
# |        1 a 10        |         R$ 10,00       |
# |       11 a 20        |         R$ 15,00       |
# |       21 a 30        |         R$ 20,00       |
# |       31 a 40        |         R$ 30,00       |
#
# |                   TABELA 2                      |
# |      Preço Total da Nota      |  % de Desconto  |
# |        Até R$ 250,00          |        5%       |
# |  Entre R$ 250,00 e R$ 500,00  |       10%       |
# |    De R$ 500,00 para cima     |       15%       |

def entry():
    code = int(input('Informe o código do produto: '))
    quantity = int(input('Informe a quantidade comprada: '))
    return code, quantity

# Função que retorna o preço unitário do produto
def unit_price(code):
    if 1 <= code <= 10:
        return 10
    if 11 <= code <= 20:
        return 15
    if 21 <= code <= 30:
        return 20
    return 30

# Função que retorna o preço total da nota
def total_price(unit_price, quantity):
    return unit_price * quantity

# Função que retorna o valor do desconto
def discount(total_price):
    if total_price <= 250:
        return total_price * 0.05
    if 250 < total_price <= 500:
        return total_price * 0.1
    return total_price * 0.15

# Função que retorna o preço final da nota depois do desconto
def final_price(total_price, discount):
    return total_price - discount

def main():
    code, quantity = entry()
    unit = unit_price(code)
    total = total_price(unit, quantity)
    discount_value = discount(total)
    final = final_price(total, discount_value)
    print(f'O preço unitário do produto é R${unit:.2f}')
    print(f'O preço total da nota é R${total:.2f}')
    print(f'O valor do desconto é R${discount_value:.2f}')
    print(f'O preço final da nota depois do desconto é R${final:.2f}')