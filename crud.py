class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

# Lista para armazenar as pessoas
pessoas = []

def criar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    pessoa = Pessoa(nome, peso, altura)
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    print("Lista de pessoas cadastradas:")
    for i, pessoa in enumerate(pessoas, start=1):
        print(f"{i}. Nome: {pessoa.nome}, Peso: {pessoa.peso} kg, Altura: {pessoa.altura} m")

def atualizar_pessoa():
    listar_pessoas()
    indice = int(input("Digite o número da pessoa que deseja atualizar: ")) - 1
    pessoa = pessoas[indice]
    print(f"Atualizando dados para {pessoa.nome}:")
    pessoa.peso = float(input("Novo peso (em kg): "))
    pessoa.altura = float(input("Nova altura (em metros): "))
    print("Dados atualizados com sucesso!")

def excluir_pessoa():
    listar_pessoas()
    indice = int(input("Digite o número da pessoa que deseja excluir: ")) - 1
    pessoa = pessoas.pop(indice)
    print(f"{pessoa.nome} foi removido da lista.")

# Menu principal
while True:
    print("\n1. Criar Pessoa")
    print("2. Listar Pessoas")
    print("3. Atualizar Pessoa")
    print("4. Excluir Pessoa")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_pessoa()
    elif opcao == "2":
        listar_pessoas()
    elif opcao == "3":
        atualizar_pessoa()
    elif opcao == "4":
        excluir_pessoa()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
