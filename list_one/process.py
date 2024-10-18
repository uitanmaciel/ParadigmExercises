import list_one.question01
import list_one.question02
import list_one.question03
import list_one.question04
import list_one.question05
import list_one.question06
import list_one.question07
import list_one.question08
import list_one.question09
import list_one.question10
import list_one.question11
import list_one.question12
import list_one.question13
import list_one.question14
import list_one.question15
import Menu.menu as menu

# Função que exibe o menu de opções
def menu_show():
    print("Qual exercício deseja executar?")
    menu.breakline()
    print("(1) Exercício 1 - Cálculo Média Aritmética de notas")
    print("(2) Exercício 2 - Cáluco Média Ponderada de notas")
    print("(3) Exercício 3 - Cálculo de salário 1")
    print("(4) Exercício 4 - Cálculo de salário 2")
    print("(5) Exercício 5 - Cálculo de salário 3")
    print("(6) Exercício 6 - Cálculo de salário 4")
    print("(7) Exercício 7 - Cálculo financeiro")
    print("(8) Exercício 8 - Cálculos matemáticos")
    print("(9) Exercício 9 - Cálculo da idade de uma pessoa (presente e futuro (2030))")
    print("(10) Exercício 10 - Cálcula do Preço de um veículo")
    print("(11) Exercício 11 - Cálculo de salário com base em horas trabalhadas")
    print("(12) Exercício 12 - Cálculo de saldo bancário")
    print("(13) Exercício 13 - Cálculo de distância de uma escada até a parede")
    print("(14) Exercício 14 - Cálculo de valor de quilowatt")
    print("(15) Exercício 15 - Cálculo de quantidade de convites para alcançar o custo total do espetáculo")
    print("(0) MENU ANTERIOR:")

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

# Função que pausa o sistema
def __system_pause():
    input("\nPressione ENTER para continuar...")

# Função que exibe o menu de exportação
def __export_menu_first():
    menu.clear_screen()
    menu.header_list_one()
    menu.breakline()

# Função que exibe o menu de exportação
def __export_menu_second():
    menu.clear_screen()
    menu.header_list_one()
    menu_show()
    menu.breakline()
    option = menu_option()
    execute_list_one(option)

# Executa a lista de exercícios 1
def execute_list_one(option):
    while True:        
        if option == 0:
            menu.clear_screen()
            menu.header_main()
            menu.options_menu()
            break
        elif option == 1:            
            __export_menu_first()
            list_one.question01.main()
            __system_pause()
            __export_menu_second()            
            break
        elif option == 2:            
            __export_menu_first()
            list_one.question02.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 3:            
            __export_menu_first()
            list_one.question03.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 4:            
            __export_menu_first()
            list_one.question04.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 5:            
            __export_menu_first()
            list_one.question05.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 6:
            __export_menu_first()
            list_one.question06.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 7:
            __export_menu_first()
            list_one.question07.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 8:
            __export_menu_first()
            list_one.question08.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 9:
            __export_menu_first()
            list_one.question09.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 10:
            __export_menu_first()
            list_one.question10.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 11:
            __export_menu_first()
            list_one.question11.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 12:
            __export_menu_first()
            list_one.question12.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 13:
            __export_menu_first()
            list_one.question13.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 14:
            __export_menu_first()
            list_one.question14.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 15:
            __export_menu_first()
            list_one.question15.main()
            __system_pause()
            __export_menu_second()
            break
        else:
            print("Opção inválida!")
            menu.options_menu()
            break