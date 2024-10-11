# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#
# 1, 2, 3, 4 	Votos para os respectivos candidatos
# 5	Voto nulo
# 6	Voto em branco
#
# Faça um algoritmo que calcule e mostre:
#
# 1. o total de votos para cada candidato;
# 2. o total de votos nulos;
# 3. o total de votos em branco;
# 4. a percentagem de votos nulos sobre o total de votos;
# 5. a percentagem de votos em branco sobre o total de votos;
#
# Para finalizar o conjunto de votos, tem-se o valor zero.

def entry():
    votes = {}
    while True:
        vote = int(input("Qual seu candidato? \n(1) Candidato A,\n(2) Candidato B,\n(3) Candidato C ou\n(4) Candidato D.\n(5) Para votar NULO\n(6) Para votar em  BRANCO ou\n(0) Para SAIR:\n"))
        if vote == 0:
            break
        if vote == 1:
            votes['A'] = votes.get('A', 0) + 1
        elif vote == 2:
            votes['B'] = votes.get('B', 0) + 1
        elif vote == 3:
            votes['C'] = votes.get('C', 0) + 1
        elif vote == 4:
            votes['D'] = votes.get('D', 0) + 1
        elif vote == 5:
            votes['NULO'] = votes.get('NULO', 0) + 1
        elif vote == 6:
            votes['BRANCO'] = votes.get('BRANCO', 0) + 1
        else:
            print("Voto inválido")

    return votes

# Calcula o total de votos
def total_votes(votes):
    total = sum(votes.values())
    return total

# Calcula os votos por candidato
def count_votes_per_candidate(votes):
    for candidate, votes in votes.items():
        if candidate == 'NULO' or candidate == 'BRANCO':
            continue
        print(f"O candidato {candidate} recebeu {votes} votos")

# Calcula os votos em branco e nulos
def count_votes_blank_and_null(votes):
    for candidate, votes in votes.items():
        if candidate == 'NULO' or candidate == 'BRANCO':
            print(f"Votos {candidate}S: {votes}")

# Calcula os votos nulos
def count_null_votes(votes):
    null_votes = votes.get('NULO', 0)
    return null_votes

# Calcula os votos em branco
def count_blank_votes(votes):
    blank_votes = votes.get('BRANCO', 0)
    return blank_votes

# Calcula a porcentagem de votos nulos
def count_percentage_null_votes(votes):
    null_votes = count_null_votes(votes)
    percentage = (null_votes / total_votes(votes)) * 100
    print(f"A percentagem de votos nulos sobre o total de votos foi de {percentage:.2f}%")

# Calcula a porcentagem de votos em branco
def count_percentage_blank_votes(votes):
    blank_votes = count_blank_votes(votes)
    percentage = (blank_votes / total_votes(votes)) * 100
    print(f"A percentagem de votos em branco sobre o total de votos foi de {percentage:.2f}%")

def main():
    votes = entry()
    count_votes_per_candidate(votes)
    count_votes_blank_and_null(votes)
    count_null_votes(votes)
    count_blank_votes(votes)
    count_percentage_null_votes(votes)
    count_percentage_blank_votes(votes)
    print(f"Total de votos: {total_votes(votes)}")