#%%
def main():
    # Armazenar idades e alturas
    idades = []
    alturas = []

    # Pedir ao usuário para inserir as idades e alturas dos alunos
    for i in range(30):
        idade = int(input("Digite a idade do aluno {i + 1}: "))
        altura = float(input("Digite a altura (em metros) do aluno {i + 1}: "))
        idades.append(idade)
        alturas.append(altura)
    # Calcular a média das alturas dos alunos com mais de 13 anos
    total_alturas = 0
    qtd_alunos = 0
    for i in range(30):
        if idades[i] > 13:
            total_alturas += alturas[i]
            qtd_alunos += 1
    if qtd_alunos == 0:
        print("Não há alunos com mais de 13 anos para se calcular a média")
        return
    media_alturas = total_alturas / qtd_alunos

    # Contar quantos alunos com mais de 13 anos têm altura inferior à média
    alunos_abaixo_da_media = 0
    for i in range(30):
        if idades[i] > 13 and alturas[i] < media_alturas:
            alunos_abaixo_da_media += 1
    # Exibir resultado
    print(f"Quantidade de alunos com mais de 13 anos e altura abaixo da média calculada: {alunos_abaixo_da_media}")

if __name__ == "__main__":
    main()
# %%
