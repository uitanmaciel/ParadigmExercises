def __enunciate():
    print('''# Uma empresa decide  dar um aumento de 30% com salários inferiores a R$ 500,00.
# Faça um algoritmo que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem,
# caso o funcionário não tenha direito ao aumento.\n''')

def entry():
    return float(input('Informe o salário do funcionário: '))

# Função que verifica se o salário é menor que 500, se for, aumenta 30%, caso contrário, retorna uma mensagem
def increase(salary):
    if salary < 500:
        return salary * 1.3
    return "O funcionário não tem direito ao aumento"

def main():
    __enunciate()
    salary = entry()
    if type(increase(salary)) == float:
        print(f'O salário reajustado é R${increase(salary):.2f}')
    else:
        print(increase(salary))