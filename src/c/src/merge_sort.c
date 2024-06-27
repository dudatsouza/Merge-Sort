// IMPLEMENTAÇÃO MERGE SORT EM C
#include "merge_sort.h"

void merge(int *v, int inicio, int meio, int fim) {
    int tamanho = fim - inicio + 1;
    int *temp = (int *) malloc(tamanho * sizeof(int));
    int p1 = inicio;
    int p2 = meio + 1;
    int fim1 = 0, fim2 = 0;
    int i, j, k;
   
    temp = (int *) malloc(tamanho * sizeof(int));
    if (temp != NULL) {
        for (i = 0; i < tamanho; i++) {
            if (!fim1 && !fim2) {
                if (v[p1] < v[p2]) {
                    temp[i] = v[p1++];
                } else {
                    temp[i] = v[p2++];
                }
                if (p1 > meio) {
                    fim1 = 1;
                }
                if (p2 > fim) {
                    fim2 = 1;
                }
            } else {
                if (!fim1) {
                    temp[i] = v[p1++];
                } else {
                    temp[i] = v[p2++];
                }
            }
        }
        for (j = 0, k = inicio; j < tamanho; j++, k++) {
            v[k] = temp[j];
        }
    }

    free(temp);
}

void mergeSort(int *v, int inicio, int fim) {
    int meio;
    if (inicio < fim) {
        meio = (inicio + fim) / 2;
        mergeSort(v, inicio, meio);
        mergeSort(v, meio + 1, fim);
        merge(v, inicio, meio, fim);
    }
}

void definirArray(int n, int *v, char *nome) {
    FILE *arq = fopen(nome, "r");
    if (arq == NULL) {
        perror("Erro ao abrir o arquivo de entrada");
        exit(EXIT_FAILURE);
    }

    int i = 0;
    for (i = 0; i < n && fscanf(arq, "%d", &v[i]) == 1; i++);

    fclose(arq);
}

void salvarTempo(int n, double time_taken, char *nome, char *nome2) {
    FILE *arq2 = fopen(nome2, "a");
    if (arq2 == NULL) {
        perror("Erro ao abrir o arquivo de saída");
        exit(EXIT_FAILURE);
    }

    fprintf(arq2, "\nC,%d,%f,%s", n, time_taken, nome);
    fclose(arq2);
}

void run(int n, char *nome, char *nome2) {
    int *v = (int *) malloc(n * sizeof(int));
    if (v == NULL) {
        perror("Erro ao alocar memória");
        exit(EXIT_FAILURE);
    }

    definirArray(n, v, nome);

    clock_t t = clock();
    mergeSort(v, 0, n - 1);
    t = clock() - t;
    double time_taken = ((double) t) / CLOCKS_PER_SEC;

    salvarTempo(n, time_taken, nome, nome2);
    printf("\nTempo de execução: %f", time_taken);
    free(v);
}
