def __enunciate():
    print('''# Questão 14 - Faça um algoritmo que receba a idade e a altura de várias pessoas e que calcule e mostre a média das alturas
# das pessoas com mais de 50 anos. Para encerrar a entrada de dados digite idade menor ou igual a zero.\n''')

def entry():
    while True:
        age = int(input("Digite a idade: "))
        if age <= 0:
            break
        height = float(input("Digite a altura: "))
        if age > 50:
            yield height

def main():
    __enunciate()
    total = 0
    count = 0
    for height in entry():
        total += height
        count += 1
    if count > 0:
        print(f"Média das alturas das pessoas com mais de 50 anos: {total/count}")
    else:
        print("Nenhuma pessoa com mais de 50 anos foi registrada.")