import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import list_one.process
import list_two.process
import list_three.process

# Cria linhas de separação e cabeçalhos para o menu
def __linebar():
    print("================================================================================")

# Cria uma quebra de linha
def breakline():
    print()

# Cria um cabeçalho para o menu principal
def header_main():
    __linebar()
    print("                 Bem-vindo ao sistema de execução de exercícios!                ")
    __linebar()
    breakline()

# Cria um subcabeçalho para o menu principal
def sub_header_main():
    print("Para executar um exercício, selecione a lista de exercícios que deseja executar.")
    breakline()

# Cria um cabeçalho para a saída do menu principal
def header_main_exit():
    __linebar()
    print("                    Obrigado por utilizar o sistema de execução                   ")
    __linebar()

# Limpa a tela do console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Cria um cabeçalho para a lista de exercícios 1
def header_list_one():
    __linebar()
    print("                              Lista de Exercícios 1                             ")
    __linebar()

# Cria um cabeçalho para a lista de exercícios 2
def header_list_two():
    __linebar()
    print("                              Lista de Exercícios 2                            ")
    __linebar()

# Cria um cabeçalho para a lista de exercícios 3
def header_list_three():
    __linebar()
    print("                              Lista de Exercícios 3                            ")
    __linebar()


def options_menu():
    while True:
        print("(1) Lista de Exercícios 1")
        print("(2) Lista de Exercícios 2")
        print("(3) Lista de Exercícios 3")
        print("(0) Sair")
        breakline()
        options = int(input("Digite a opção desejada: "))
        if options == 0:
            clear_screen()
            header_main_exit()
            break
        elif options == 1:
            clear_screen()
            header_list_one()            
            breakline()            
            list_one.process.menu_show()
            breakline()
            option = list_one.process.menu_option()
            breakline()
            list_one.process.execute_list_one(option)            
        elif options == 2:
            clear_screen()
            header_list_two()            
            breakline()            
            list_two.process.menu_show()
            breakline()
            option = list_two.process.menu_option()
            breakline()
            list_two.process.execute_list_two(option)
        elif options == 3:
            clear_screen()
            header_list_three()            
            breakline()            
            list_three.process.menu_show()
            breakline()
            option = list_three.process.menu_option()
            breakline()
            list_three.process.execute_list_three(option)            
        else:
            print("Opção inválida. Tente novamente.")
            breakline()
            continue
        break