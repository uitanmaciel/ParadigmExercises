# O custo ao consumidor de um carro novo é a soma do preço de fábrica com o # percentual  de lucro do distribuidor
# e dos impostos aplicados ao preço de fábrica. Faça um algoritmo que receba o # preço de fábrica de um veículo,
# o percentual de lucro do distribuidor e o percentual de impostos. Calcule e mostre:
#
# a)	o valor correspondente ao lucro do distribuidor;
# b)	o valor correspondente aos impostos;
# c)	o preço final do veículo;

def entry ():
    factory_price = float(input("Informe o preço de fábrica do veículo: "))
    profit_percentage = float(input("Informe o percentual de lucro do distribuidor: "))
    taxes_percentage = float(input("Informe o percentual de impostos: "))
    return factory_price, profit_percentage, taxes_percentage

# Calcula o lucro do distribuidor
def calculate_profit (factory_price, profit_percentage):
    return factory_price * (profit_percentage / 100)

# Calcula os impostos
def calculate_taxes (factory_price, taxes_percentage):
    return factory_price * (taxes_percentage / 100)

# Calcula o preço final do veículo
def calculate_final_price (factory_price, profit, taxes):
    return factory_price + profit + taxes

def main ():
    factory_price, profit_percentage, taxes_percentage = entry()
    profit = calculate_profit(factory_price, profit_percentage)
    taxes = calculate_taxes(factory_price, taxes_percentage)
    final_price = calculate_final_price(factory_price, profit, taxes)
    print(f"O valor correspondente ao lucro do distribuidor é: R$ {profit:.2f}")
    print(f"O valor correspondente aos impostos é: R$ {taxes:.2f}")
    print(f"O preço final do veículo é: R$ {final_price:.2f}")