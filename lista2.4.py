#%%
# Crie um programa que leia as notas da 1° e 2° avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
num1 = int(input("Digite a primeira nota: "))
num2 = int(input("Digite a segunda nota:  "))
soma = num1 + num2
if soma == 6:
    print("Aprovado")
elif soma > 6:
    print("Parabéns!")
else:
    print("Reprovado!")
# %%
