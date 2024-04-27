#%%
# Faça um programa que receba um número e que calcule e mostre a tabuada desse número
numero = int(input("Digite um número: "))

def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        print()

for numero in range(1, 11):
    tabuada(numero)
# %%
