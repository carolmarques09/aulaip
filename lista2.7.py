#%%
# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem "Saldo Positivo", senão escrever a mensagem "Saldo Negativo"
def calcular_saldo_atual(saldo, débito, crédito):
    saldo_atual = saldo - débito + crédito
if saldo_atual >= 0:
    print('Saldo Positivo')
else:
    print('Saldo Negativo')

# Função principal
def main():
    # Ler os valores da conta do cliente, saldo, débito e crédito
    numero_conta = input("Digite o número da conta do cliente: ")
    saldo = float(input("Digite o saldo atual: "))
    debito = float(input("Digite o débito: "))
    credito = float(input("Digite o crédito: "))

    # Calcular o saldo atual e verificar se é positivo ou negativo
    saldo_atual, mensagem = calcular_saldo_atual(saldo, debito, credito)

    # Escrever o saldo atual e a mensagem
    print(f"O saldo atual da conta {numero_conta} é: {saldo_atual}")
    print(mensagem)

# Chamar a função principal
if __name__ == "__main__":
    main()
# %%
