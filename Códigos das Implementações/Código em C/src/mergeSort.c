// IMPLEMENTAÇÃO MERGE SORT EM C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void merge(int *v, int inicio, int meio, int fim) {
    int *temp, p1, p2, tamanho, i, j, k;
    int fim1 = 0, fim2 = 0;
    tamanho = fim - inicio + 1;
    p1 = inicio;
    p2 = meio + 1;
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
    FILE *arq;
    arq = fopen(nome, "r");
    if (arq == NULL) {
        printf("Erro na abertura do arquivo\n");
        return;
    }

    int i = 0;
    while (fscanf(arq, "%d", &v[i]) != EOF) {
        i++;
        if (i-1 == n) {
            break;
        }
    }
    fclose(arq);
}

void salvarTempo(int n, double time_taken, char *nome2) {
    FILE *arq2;
    arq2 = fopen(nome2, "a");
    if (arq2 == NULL) {
        printf("Erro na abertura do arquivo\n");
        return;
    }
    fprintf(arq2, "\nC,%d,%f", n, time_taken);
    fclose(arq2);
}

void run(int n, char *nome, char *nome2) {
    int v[n];
    definirArray(n, v, nome);
        
    clock_t t;
    t = clock();
    mergeSort(v, 0, n - 1);
    t = clock() - t;
    double time_taken = ((double) t) / CLOCKS_PER_SEC;

    salvarTempo(n, time_taken, nome2);
}

int main() {
    printf("Digite o tamanho do vetor: ");
    int n;
    scanf("%d", &n);

    printf("Digite o nome do arquivo de entrada: ");
    char arqE[1000];
    scanf("%s", arqE);
    
    printf("Digite o nome do arquivo de saída: ");
    char arqS[1000];
    scanf("%s", arqS);

    run(n, arqE, arqS);

    printf("Execução em C finalizada\n");
    return 0;
}

