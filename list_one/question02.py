def __enunciate():
    print("# Questão 02 - Faça um algoritmo que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas.")

def entry ():
    i = 1
    notes = []
    weights = []
    while i <= 3:
        note = float(input(f"Infome a {i}ª nota: "))
        if 0 <= note <= 10:
            notes.append(note)
            weight = float(input(f"Informe o peso da {i}ª nota: "))
            if 0 <= weight <= 10:
                weights.append(weight)
                i += 1
            else:
                print("Peso inválido. Informe um peso entre 0 e 10.")
        else:
            print("Nota inválida. Informe uma nota entre 0 e 10.")
    return notes, weights

# Calcula a média ponderada:
def weighted_average (notes, weights):
    return sum([note * weight for note, weight in zip(notes, weights)]) / sum(weights)

#Outra forma de fazer o cálculo da média ponderada:
#def weighted_average (notes, weights):
#    sum_notes = 0
#    sum_weights = 0
#    for i in range(len(notes)):
#        sum_notes += notes[i] * weights[i]
#        sum_weights += weights[i]
#    return sum_notes / sum_weights

def main ():
    __enunciate()
    print()
    notes, weights = entry()
    notes_weighted_average = weighted_average(notes, weights)
    print(f"A média ponderada das notas é: {notes_weighted_average:.2f}")