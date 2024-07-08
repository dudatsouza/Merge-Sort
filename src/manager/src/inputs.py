import random

def aleatorio(n):
    file = open(f"../../../datasets/inputs/random.txt", "w")
    for i in range(n):
        file.write(f"{random.randint(0, 1000)} ")
    file.close()


def crescente(n):
    file = open(f"../../../datasets/inputs/ascending.txt", "w")
    for i in range(n):
        file.write(f"{i} ")
    file.close()    

def decrescente(n):
    file = open(f"../../../datasets/inputs/descending.txt", "w")
    for i in range(n, 0, -1):
        file.write(f"{i} ")
    file.close()


def quase_ordenado_crescente(n):
    file = open(f"../../../datasets/inputs/nearly_sorted_ascending.txt", "w")
    for i in range(n):
        file.write(f"{i} ")
    for i in range(n//10):
        file.write(f"{random.randint(0, n)} ")
    file.close()

def quase_ordenado_decrescente(n):
    file = open(f"../../../datasets/inputs/nearly_sorted_descending.txt", "w")
    for i in range(n, 0, -1):
        file.write(f"{i} ")
    for i in range(n//10):
        file.write(f"{random.randint(0, n)} ")
    file.close()

def main():
    print("-----------------------------")
    print("GERADOR DE ENTRADAS\n")
    print("Serão gerados 5 arquivos de entradas ordenados de forma diferente (aleatório, crescente, decrescente, quase ordenado crescente e quase ordenado decrescente)." )
    n = 1000000
    aleatorio(n)
    crescente(n)
    decrescente(n)
    quase_ordenado_crescente(n)
    quase_ordenado_decrescente(n)
    print("\nArquivos gerados com sucesso!")
    print("-----------------------------")

if __name__ == "__main__":
    main()