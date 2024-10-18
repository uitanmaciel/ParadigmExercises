def __enunciate():
    print("# Questão 01 - Faça um algoritmo que receba três notas, calcule e mostre a média aritmética entre elas.")

def entry ():
    i = 1
    notes = []
    while i <= 3:
        note = float(input(f"Infome a {i}ª nota: "))
        if 0 <= note <= 10:
            notes.append(note)
            i += 1
        else:
            print("Nota inválida. Informe uma nota entre 0 e 10.")
    return notes

# Função que calcula a média aritmética das notas
def average (notes):
    return sum(notes) / len(notes)

def main ():
    __enunciate()
    print()
    notes = entry()
    notes_average = average(notes)
    print(f"A média das notas é: {notes_average:.2f}")