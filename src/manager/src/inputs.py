import random

def aleatorio(n):
    file = open(f"../../datasets/Entradas/aleatorio.txt", "w")
    for i in range(n):
        file.write(f"{random.randint(0, 1000)} ")
    file.close()


def crescente(n):
    file = open(f"../../datasets/Entradas/crescente.txt", "w")
    for i in range(n):
        file.write(f"{i} ")
    file.close()    

def decrescente(n):
    file = open(f"../../datasets/Entradas/decrescente.txt", "w")
    for i in range(n, 0, -1):
        file.write(f"{i} ")
    file.close()


def quase_ordenado(n):
    file = open(f"../../datasets/Entradas/quase_ordenado.txt", "w")
    for i in range(n):
        file.write(f"{i} ")
    file.write(f"{random.randint(0, 1000)} ")
    file.close()


def main():
    print("-----------------------------")
    print("GERADOR DE ENTRADAS\n")
    print("Serão gerados 4 arquivos de entradas ordenados de forma diferente (aleatório, crescente, decrescente e quase ordenado)")
    n = 1000000
    aleatorio(n)
    crescente(n)
    decrescente(n)
    quase_ordenado(n)
    print("\nArquivos gerados com sucesso!")
    print("-----------------------------")

if __name__ == "__main__":
    main()