#%%
# Função para fazer cadastro de usuário, com nome, idade e e-mail.

def cadastrar_usuario():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    email = input("Digite o seu e-mail: ")

    # Abrir um arquivo em modo de escrita
    with open("usuarios.txt", "a") as arquivo:
        # Escrever os dados do usuário no arquivo, separados por vírgula
        arquivo.write(f"{nome},{idade},{email}\n")

    print("Usuário cadastrado com sucesso!")

def main():
    print("Cadastro de Usuário")
    while True:
        cadastrar = input("Deseja cadastrar um usuário? (s/n): ")
        if cadastrar.lower() == 's':
            cadastrar_usuario()
        elif cadastrar.lower() == 'n':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()

# %%
