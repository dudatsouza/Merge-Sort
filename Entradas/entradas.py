import random

def aleatorio(n):
    file = open(f"../Entradas/datasets/aleatorio.txt", "w")
    for i in range(n):
        file.write(f"{random.randint(0, 1000)} ")
    file.close()


def crescente(n):
    file = open(f"../Entradas/datasets/crescente.txt", "w")
    for i in range(n):
        file.write(f"{i} ")
    file.close()    

def decrescente(n):
    file = open(f"../Entradas/datasets/decrescente.txt", "w")
    for i in range(n, 0, -1):
        file.write(f"{i} ")
    file.close()


def quase_ordenado(n):
    file = open(f"../Entradas/datasets/quase_ordenado.txt", "w")
    for i in range(n):
        file.write(f"{i} ")
    file.write(f"{random.randint(0, 1000)} ")
    file.close()


def main():
    print("Serão gerados 4 arquivos de entradas ordenados de forma diferente (aleatório, crescente, decrescente e quase ordenado)")
    n = 1000000
    aleatorio(n)
    crescente(n)
    decrescente(n)
    quase_ordenado(n)
    print("Arquivos gerados com sucesso!")

if __name__ == "__main__":
    main()