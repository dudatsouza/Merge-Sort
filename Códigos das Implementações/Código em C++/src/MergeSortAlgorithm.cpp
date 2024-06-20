// IMPLEMENTAÇÃO MERGE SORT EM C++
#include "MergeSortAlgorithm.hpp"

MergeSortAlgorithm::MergeSortAlgorithm(const string &arqE, const string &arqS)
    : arq(arqE), arq2(arqS) {}

void MergeSortAlgorithm::merge(vector<int>& v, int inicio, int meio, int fim) {
    int tamanho = fim - inicio + 1;
    vector<int> temp(tamanho);
    int p1 = inicio, p2 = meio + 1, idx = 0;

    while (p1 <= meio && p2 <= fim) {
        if (v[p1] <= v[p2]) {
            temp[idx++] = v[p1++];
        } else {
            temp[idx++] = v[p2++];
        }
    }

    while (p1 <= meio) {
        temp[idx++] = v[p1++];
    }

    while (p2 <= fim) {
        temp[idx++] = v[p2++];
    }

    for (int i = 0; i < tamanho; ++i) {
        v[inicio + i] = temp[i];
    }
}

void MergeSortAlgorithm::mergeSort(vector<int>& v, int inicio, int fim) {
    int meio;
    if (inicio < fim) {
        meio = (inicio + fim) / 2;
        mergeSort(v, inicio, meio);
        mergeSort(v, meio + 1, fim);
        merge(v, inicio, meio, fim);
    }
}

void MergeSortAlgorithm::definirArray(int n) {
    ifstream file(arq);
    if (!file.is_open()) {
        cerr << "Erro ao abrir o arquivo de entrada.\n";
        return;
    }

    array.clear(); 
    int num;
    while (file >> num) {
        array.push_back(num);
    }
    file.close();

    if (array.size() > n) {
        array.resize(n);
    }
}

void MergeSortAlgorithm::salvarTempo(int n, double timeTaken) {
    ofstream file(arq2, ios::app);
    if (!file.is_open()) {
        cerr << "Erro ao abrir o arquivo de saída.\n";
        return;
    }
    file << "\nC++," << n << "," << fixed << setprecision(10) << timeTaken << "," << arq;
    file.close();
}

void MergeSortAlgorithm::run(int n) {
    definirArray(n);

    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    mergeSort(array, 0, array.size() - 1);
    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    duration<double> time_span = duration_cast<duration<double>>(t2 - t1);
    salvarTempo(n, time_span.count());
}
