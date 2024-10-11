# Faça um algoritmo para calcular e mostrar a que distância deve estar uma escada da parede.
# O usuário deve fornecer o tamanho da escada e a altura em que se deseja pregar o quadro.

def entry ():
    ladder_size = float(input("Informe o tamanho da escada (em metros): "))
    height = float(input("Informe a altura em que deseja pregar o quadro (em metros): "))
    return ladder_size, height

# Calcula a distância da base da escada até a parede usando o Teorema de Pitágoras
def calculate_distance (ladder_size, height):
    if ladder_size <= height:
        return print("O tamanho da escada deve ser maior que a altura em que deseja pregar o quadro.")
    return (ladder_size ** 2 - height ** 2) ** 0.5

def main ():
    ladder_size, height = entry()
    distance = calculate_distance(ladder_size, height)
    if distance:
        print(f"A distância da base da escada até a parede deve ser de {distance:.2f} metros.")