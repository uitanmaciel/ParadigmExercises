import list_two.question01
import list_two.question02
import list_two.question03
import list_two.question04
import list_two.question05
import list_two.question06
import list_two.question07
import list_two.question08
import list_two.question09
import list_two.question10
import Menu.menu as menu

# Função que exibe o menu de opções
def menu_show():
    print("Qual exercício deseja executar?")
    menu.breakline()
    print("1 - Exercício 1 - Verifica se o aluno foi aprovado ou reprovado 1")
    print("2 - Exercício 2 - Verifica se o aluno foi aprovado ou reprovado 2")
    print("3 - Exercício 3 - Calcula a média entre dois números")
    print("4 - Exercício 4 - Clacula se um funcionário tem diretiro a aumento de salário")
    print("5 - Exercício 5 - Calcula o valor do crédito de um cliente")
    print("6 - Exercício 6 - Calcula e classifica o preço de um produto")
    print("7 - Exercício 7 - Classifica a categoria de um nadador")
    print("8 - Exercício 8 - Classifica a procedência de um produto")
    print("9 - Exercício 9 - Classifica o grupo de risco de uma pessoa")
    print("10 - Exercício 10 - Calcula o preço de um produto comprado")
    print("0 - MENU ANTERIOR:")

# Função que permite a escolha de uma opção do menu
def menu_option():
    while True:
        option = int(input("Digite a opção desejada: "))
        if option == 0:
            menu.clear_screen()
            menu.header_main()
            menu.options_menu()
            break
        elif option > 0 and option <= 15:
            return option
        else:
            print("Opção inválida!")
            break

def __system_pause():
    input("\nPressione ENTER para continuar...")

# Função que exibe o menu de exportação
def __export_menu_first():
    menu.clear_screen()
    menu.header_list_two()
    menu.breakline()

# Função que exibe o menu de exportação
def __export_menu_second():
    menu.clear_screen()
    menu.header_list_two()
    menu_show()
    menu.breakline()
    option = menu_option()
    execute_list_two(option)

def execute_list_two(option):
    while True:        
        if option == 0:
            menu.clear_screen()
            menu.header_main()
            menu.options_menu()
            break
        elif option == 1:            
            __export_menu_first()
            list_two.question01.main()
            __system_pause()
            __export_menu_second()            
            break
        elif option == 2:            
            __export_menu_first()
            list_two.question02.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 3:            
            __export_menu_first()
            list_two.question03.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 4:            
            __export_menu_first()
            list_two.question04.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 5:            
            __export_menu_first()
            list_two.question05.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 6:
            __export_menu_first()
            list_two.question06.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 7:
            __export_menu_first()
            list_two.question07.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 8:
            __export_menu_first()
            list_two.question08.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 9:
            __export_menu_first()
            list_two.question09.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 10:
            __export_menu_first()
            list_two.question10.main()
            __system_pause()
            __export_menu_second()
            break
        else:
            print("Opção inválida!")
            menu.options_menu()
            break