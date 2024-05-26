# Importacao das bibliotecas

import tkinter as tk
from tkinter import ttk
from tkinter import *

dados = []

# Inicializando a interface gráfica
# Criando a janela (root) principal

root = tk.Tk()
root.geometry("300x400")
root.title("Calculadora de IMC")
root.configure(bg="black")
fonte = ("Arial", 10)

# Criando os campos de entrada
entrada_nome = tk.Entry(root)
entrada_idade = tk.Entry(root)
entrada_peso = tk.Entry(root)
entrada_altura = tk.Entry(root)
entrada_imc = tk.Entry(root)

# Função para criar o arquivo .txt
def criar_pessoa():
    with open("dados.txt", "w") as arquivo:
        arquivo.write("")

# Função para ler o arquivo .txt
def ler_pessoa():
    with open("dados.txt", "r") as arquivo:
        dados = arquivo.readlines()
    return dados

# Função para inserir um registro no arquivo .txt
def inserir_pessoa():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    peso = entrada_peso.get()
    altura = entrada_altura.get()
    with open("dados.txt", "a") as arquivo:
        arquivo.write("\n" + ",".join([str(elemento) for elemento in dados]))


# Função para excluir um registro no arquivo .txt
def excluir_pessoa():
    imc = entrada_imc.get()
    dados = ler_pessoa()
    for i in range(len(dados)):
        linha = dados[i].strip()
        if linha.startswith(imc):
            del dados[i]
    with open("dados.txt", "w") as arquivo:
        arquivo.writelines(dados)

# Função para exibir os registros do arquivo .txt
def exibir_pessoa():
    dados = ler_pessoa()
    for linha in dados:
        linha = linha.strip()
        if linha:
            print(linha)


# Criando os botões
botao_criar = tk.Button(root, text="Inserir", command=inserir_pessoa)
botao_ler = tk.Button(root, text="Ler", command=exibir_pessoa)
botao_excluir = tk.Button(root, text="Excluir", command=excluir_pessoa)

# Adicionando os campos de entrada e os botões à interface gráfica
entrada_nome.grid(row=0, column=0)
entrada_idade.grid(row=1, column=0)
entrada_peso.grid(row=1, column=0)
entrada_altura.grid(row=1, column=0)
botao_criar.grid(row=7, column=0)
botao_ler.grid(row=8, column=0)
botao_excluir.grid(row=10, column=0)

# Definição da declaração das variaveis e das entradas dos dados

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def exibir_classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"
    
def cadastrar_pessoa():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())

    imc = calcular_imc(peso, altura)
    classificacao = exibir_classificacao_imc(imc)

# Exibe o resultado das variaveis digitadas nos widgets

    resultado_label.config(text=f" Nome: {nome} \n Idade: {idade} anos \n Peso: {peso} kg"
                                f"\n Altura: {altura} m \n IMC : {imc:.2f}")
    classificacao_label.config(text=f"A classificação é: {classificacao}")

# Cria os widgets(Botoes)
nome_label = ttk.Label(root, text="Nome (Paciente):")
nome_entry = ttk.Entry(root)

idade_label = ttk.Label(root, text="Idade (Anos):")
idade_entry = ttk.Entry(root)

peso_label = ttk.Label(root, text="Peso(kg):")
peso_entry = ttk.Entry(root)

altura_label = ttk.Label(root, text="Altura(m):")
altura_entry = ttk.Entry(root)

calcular_button = ttk.Button(root, text="Calcular IMC", command=cadastrar_pessoa)

resultado_label = ttk.Label(root, text="")
classificacao_label = ttk.Label(root, text="")

# Posiciona os widgets na janela (ou também chamado de root, que é a janela principal) (Local pra digitar os dados)
nome_label.grid(row=0, column=0, padx=10, pady=5)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

idade_label.grid(row=1, column=0, padx=10, pady=5)
idade_entry.grid(row=1, column=1, padx=10, pady=5)

peso_label.grid(row=2, column=0, padx=10, pady=5)
peso_entry.grid(row=2, column=1, padx=10, pady=5)

altura_label.grid(row=3, column=0, padx=10, pady=5)
altura_entry.grid(row=3, column=1, padx=10, pady=5)

calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

resultado_label.grid(row=5, column=0, columnspan=2, pady=5)
classificacao_label.grid(row=6, column=0, columnspan=2, pady=5)

# Inicia o loop principal da interface grafica

root.mainloop()









