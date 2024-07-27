// IMPLEMENTAÇÃO MERGE SORT EM C
#include "merge_sort.h"

int main() {
    printf("Digite o tamanho do vetor: ");
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "Entrada inválida para o tamanho do vetor.\n");
        return EXIT_FAILURE;
    }

    printf("Digite o nome do arquivo de entrada: ");
    char arqE[1000];
    if (scanf("%999s", arqE) != 1) {
        fprintf(stderr, "Entrada inválida para o nome do arquivo de entrada.\n");
        return EXIT_FAILURE;
    }

    printf("Digite o nome do arquivo de saída: ");
    char arqS[1000];
    if (scanf("%999s", arqS) != 1) {
        fprintf(stderr, "Entrada inválida para o nome do arquivo de saída.\n");
        return EXIT_FAILURE;
    }

    run(n, arqE, arqS);

    printf("\nExecução em C finalizada\n");
    return;
}
