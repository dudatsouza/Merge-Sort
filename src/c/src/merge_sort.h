// IMPLEMENTAÇÃO MERGE SORT EM C
#ifndef MERGE_SORT_H
#define MERGE_SORT_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void merge(int *v, int inicio, int meio, int fim);
void mergeSort(int *v, int inicio, int fim);
void definirArray(int n, int *v, char *nome);
void salvarTempo(int n, double time_taken, char *nome, char *nome2);
void run(int n, char *nome, char *nome2);

#endif // MERGE_SORT_H

