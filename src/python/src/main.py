# IMPLEMENTAÇÃO MERGE SORT EM PYTHON
from MergeSort import MergeSort

def main():
    try:
        n = int(input("Digite o tamanho do vetor: "))
        if n <= 0:
            raise ValueError("Tamanho do vetor deve ser um número positivo.")
    except ValueError as ve:
        print(f"Entrada inválida: {ve}")
        return

    arqE = input("Digite o nome do arquivo de entrada: ")
    arqS = input("Digite o nome do arquivo de saída: ")

    sorter = MergeSort(arqE, arqS)
    sorter.run(n)

    print("Execução em Python finalizada")

if __name__ == "__main__":
    main()
