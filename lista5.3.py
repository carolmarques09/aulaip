#%%
# Programa que peça as quatro notas de 10 alunos
def calcular_media(notas):
    return sum(notas) / len(notas)

alunos = 10
medias = []

# Pedir as notas de cada aluno
for i in range(alunos):
    notas = []
    print(f"Informe as notas do aluno {i + 1}:")
    for j in range(4):
        nota = float(input(f"Nota {j + 1}:"))
        notas.append(nota)
    media = calcular_media(notas)
    medias.append(media)

# Contar o número de alunos com média maior ou igual a 7.0
numero_alunos_aprovados = sum(1 for media in medias if media >= 7.0)

print(f"O número de alunos com média maior ou igual a 7.0: {numero_alunos_aprovados}")