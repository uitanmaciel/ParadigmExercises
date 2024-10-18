def __enunciate():
    print('''# Questão 15 - Faça um algoritmo que receba o custo total de um espetáculo teatral e o preço do 
# convite  desse espetáculo. Esse algoritmo deve calcular e mostrar a quantidade de convites que devem ser 
# vendidos para que pelo menos o custo do espetáculo seja alcançado.''')

def entry ():
    total_cost = float(input("Informe o custo total do espetáculo: "))
    ticket_price = float(input("Informe o preço do convite: "))
    return total_cost, ticket_price

# Calcula a quantidade de convites que devem ser vendidos para alcançar o custo total do espetáculo
def calculate_tickets (total_cost, ticket_price):
    return total_cost / ticket_price

def main ():
    __enunciate()
    print()
    total_cost, ticket_price = entry()
    tickets = calculate_tickets(total_cost, ticket_price)
    print(f"Deve-se vender {tickets:.0f} convites para alcançar o custo total do espetáculo.")