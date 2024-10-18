import list_three.question01
import list_three.question02
import list_three.question03
import list_three.question04
import list_three.question05
import list_three.question06
import list_three.question07
import list_three.question08
import list_three.question09
import list_three.question10
import list_three.question11
import list_three.question12
import list_three.question13
import list_three.question14
import list_three.question15
import Menu.menu as menu

# Função que exibe o menu de opções
def menu_show():
    print("Qual exercício deseja executar?")
    menu.breakline()
    print("1 - Exercício 01 - Calcular números cujo o resto seja igual a 5 num sequência entre 1000 e 2000")    
    print("2 - Exercício 02 - Calcular a quantidade de pessoas com idade maior ou igual a 18 anos")
    print("3 - Exercício 03 - Calcular a tabuada de um número")
    print("4 - Exercício 04 - Calcular o valor total das compras à vista e à prazo")
    print("5 - Exercício 05 - Calcular a quantidade de pessoas com idade superior a 50 anos, a média das alturas das pessoas com idade entre 10 e 20 anos e a porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas")
    print("6 - Exercício 06 - Calcular a quantidade de pessoas com mais de 90 quilos e a média das idades das sete pessoas")
    print("7 - Exercício 07 - Calcular a quantidade de números entre 30 e 90")
    print("8 - Exercício 08 - Calcular a soma dos números pares e primos")
    print("9 - Exercício 09 - Calcular a média dos pesos das pessoas da mesma faixa etária")
    print("10 - Exercício 10 - Calcular a média das idades")
    print("11 - Exercício 11 - Calcular a média do salário da população, a média do número de filhos, o maior salário e a porcentagem de pessoas com salários até R$ 150,00")
    print("12 - Exercício 12 - Calcular a média dos salários por sexo, a maior e menor idade do grupo, a quantidade de mulheres com salário até R$ 200,00 e a idade e o sexo da pessoa que possui o menor salário")
    print("13 - Exercício 13 - Calcular o total de votos para cada candidato, o total de votos nulos, o total de votos em branco, a percentagem de votos nulos sobre o total de votos e a percentagem de votos em branco sobre o total de votos")
    print("14 - Exercício 14 - Calcular a média das alturas das pessoas com mais de 50 anos")
    print("15 - Exercício 15 - Calcular o maior e o menor valor de um conjunto de valores inteiros e positivos")
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
    menu.header_list_three()
    menu.breakline()

# Função que exibe o menu de exportação
def __export_menu_second():
    menu.clear_screen()
    menu.header_list_three()
    menu_show()
    menu.breakline()
    option = menu_option()
    execute_list_three(option)

def execute_list_three(option):
    while True:        
        if option == 0:
            menu.clear_screen()
            menu.header_main()
            menu.options_menu()
            break
        elif option == 1:            
            __export_menu_first()
            list_three.question01.main()
            __system_pause()
            __export_menu_second()            
            break
        elif option == 2:            
            __export_menu_first()
            list_three.question02.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 3:            
            __export_menu_first()
            list_three.question03.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 4:            
            __export_menu_first()
            list_three.question04.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 5:            
            __export_menu_first()
            list_three.question05.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 6:
            __export_menu_first()
            list_three.question06.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 7:
            __export_menu_first()
            list_three.question07.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 8:
            __export_menu_first()
            list_three.question08.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 9:
            __export_menu_first()
            list_three.question09.main()
            __system_pause()
            __export_menu_second()
            break
        elif option == 10:
            __export_menu_first()
            list_three.question10.main()
            __system_pause()
            __export_menu_second()
            break
        else:
            print("Opção inválida!")
            menu.options_menu()
            break