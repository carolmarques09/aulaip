#%%
# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
num1 = int(input("Digite a primeira nota: "))
num2 = int(input("Digite a segunda nota:  "))
soma = num1 + num2
if 9.0 <= soma <= 10.0:
    print("A")
elif 7.5 <= soma <= 9.0:
    print("B")
elif 6.0 <= soma <= 7.5:
    print("C")
elif 4.0 <= soma <= 6.0:
    print("D")
elif 0.0 <= soma <= 4.0:
    print("E")