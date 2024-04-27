#%%
# Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
lista = ['Dev Patel', 'Tinie T', 'Peter Criss', 'George Harrison', 'Tony Iommi']

# Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
nome = input("Digite o nome do convidado: ")
print("Você está convidado(a) para o jantar em minha casa", nome)

# Imprima o nome das pessoas que não poderão comparecer
lista2 = ['George Harrison', 'Peter Criss']
del lista[2]
del lista[3]

# Novos convidados
lista.insert(2, 'Nana Komatsu')
lista.insert(3, 'Paras Patel')

# Novo convite para cada pessoa que continua presente na lista
nome = input("Digite o nome do convidado: ")
print("Eu, você, música boa e churrasco, você está convidado(a)", nome)