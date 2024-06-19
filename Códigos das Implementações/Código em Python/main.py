from MergeSortAlgorithm import MergeSortAlgorithm

def main():
    n1 = input("Digite o tamanho do vetor: ")
    n = int(n1)

    arqE = input("Digite o nome do arquivo de entrada: ")
    arqS = input("Digite o nome do arquivo de saída: ")

    sorter = MergeSortAlgorithm(arqE, arqS)
    sorter.run(n)

    print("Execução em Python finalizada")

if __name__ == "__main__":
    main()
