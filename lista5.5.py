#%%
# Ler vetor de 5 números inteiros e mostrá-los
def main():
    vetor = []
    for i in range(5):
        num = int(input(f"Digite o {i+1}° número inteiro: "))
        vetor.append(num)
    
    print("\nNúmeros digitados: ")
    for num in vetor:
        print(num)
    
if __name__ == "__main__":
    main()