# IMPLEMENTAÇÃO MERGE SORT EM PYTHON
import time

class MergeSort:
    def __init__(self, arqE, arqS):
        self.arq = arqE
        self.arq2 = arqS
        self.array = []

    def merge(self, v, inicio, meio, fim):
        temp = []
        p1 = inicio
        p2 = meio + 1

        while p1 <= meio and p2 <= fim:
            if v[p1] <= v[p2]:
                temp.append(v[p1])
                p1 += 1
            else:
                temp.append(v[p2])
                p2 += 1

        while p1 <= meio:
            temp.append(v[p1])
            p1 += 1

        while p2 <= fim:
            temp.append(v[p2])
            p2 += 1

        for i in range(len(temp)):
            v[inicio + i] = temp[i]

    def merge_sort(self, v, inicio, fim):
        if inicio < fim:
            meio = (inicio + fim) // 2
            self.merge_sort(v, inicio, meio)
            self.merge_sort(v, meio + 1, fim)
            self.merge(v, inicio, meio, fim)

    def definir_array(self, n):
        with open(self.arq, 'r') as f:
            linha = f.readline().strip()
            numeros = list(map(int, linha.split()))
            self.array = numeros[:n]

    def salvar_tempo(self, n, tempo_decorrido):
        with open(self.arq2, 'a') as f:
            f.write(f"\nPython,{n},{tempo_decorrido:.10f},{self.arq}")
        print(f"Tempo de execução: {tempo_decorrido:.10f}")

    def run(self, n):
        self.definir_array(n)

        inicio = time.time()
        self.merge_sort(self.array, 0, len(self.array) - 1)
        fim = time.time()
        tempo_decorrido = fim - inicio

        self.salvar_tempo(n, tempo_decorrido)
