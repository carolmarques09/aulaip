#%%
# Faça um programa que mostre as tabuadas dos números de 1 a 10.
# Função para mostrar a tabuada de um número específico
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()

# Loop para mostrar as tabuadas de 1 a 10
for numero in range(1, 11):
    tabuada(numero)
# %%
