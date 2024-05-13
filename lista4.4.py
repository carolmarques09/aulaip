#%%
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
def calcular_salario_por_hora():
    try:
        salario_por_hora = int(input("Digite quanto você ganha por hora: "))
        horas_trabalhadas = int(input("Digite quantas horas trabalhadas no mês: "))

        salario_total = salario_por_hora * horas_trabalhadas

        print("Seu salário total no mês é: R$", salario_total)
    except ValueError:
        print("Por favor, insira números válidos para o salário por hora e as horas de trabalho")

calcular_salario_por_hora()
# %%
