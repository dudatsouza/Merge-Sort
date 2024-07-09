import random
import numpy as np
import secrets

def aleatorio1(n):
    file = open(f"../../../datasets/inputs/random1.txt", "w")
    for i in range(n):
        file.write(f"{random.randint(0, 1000000)} ")
    file.close()

def aleatorio2(n):
    file = open(f"../../../datasets/inputs/random2.txt", "w")
    for i in range(n):
        file.write(f"{np.random.randint(0, 1000000)} ")
    file.close()

def aleatorio3(n):
    file = open(f"../../../datasets/inputs/random3.txt", "w")
    for i in range(n):
        file.write(f"{secrets.randbelow(1000000)} ")
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
    print("Serão gerados 7 arquivos de entradas ordenados de forma diferente (aleatório1, aleatório2, aleatório3, crescente, decrescente, quase ordenado crescente e quase ordenado decrescente)." )
    n = 1000000
    aleatorio1(n)
    aleatorio2(n)
    aleatorio3(n)
    crescente(n)
    decrescente(n)
    quase_ordenado_crescente(n)
    quase_ordenado_decrescente(n)
    print("\nArquivos gerados com sucesso!")
    print("-----------------------------")

if __name__ == "__main__":
    main()