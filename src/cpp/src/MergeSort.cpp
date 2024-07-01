// IMPLEMENTAÇÃO MERGE SORT EM C++
#include "MergeSort.hpp"

MergeSort::MergeSort(std::string &arqE, std::string &arqS)
    : arq(arqE), arq2(arqS) {}

void MergeSort::merge(std::vector<int>& v, int inicio, int meio, int fim) {
    int tamanho = fim - inicio + 1;
    std::vector<int> temp(tamanho);
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

void MergeSort::mergeSort(std::vector<int>& v, int inicio, int fim) {
    int meio;
    if (inicio < fim) {
        meio = (inicio + fim) / 2;
        mergeSort(v, inicio, meio);
        mergeSort(v, meio + 1, fim);
        merge(v, inicio, meio, fim);
    }
}

void MergeSort::definirArray(int n) {
    std::ifstream file(arq);
    if (!file.is_open()) {
        std::cerr << "Erro ao abrir o arquivo de entrada.\n";
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

void MergeSort::salvarTempo(int n, double timeTaken) {
    std::ofstream file(arq2, std::ios::app);
    if (!file.is_open()) {
        std::cerr << "Erro ao abrir o arquivo de saída.\n";
        return;
    }
    file << "\nC++," << n << "," << std::fixed << std::setprecision(10) << timeTaken << "," << arq;
    std::cout << "\nTempo de execução: " << std::fixed << std::setprecision(10) << timeTaken << std::endl;
    file.close();
}

void MergeSort::run(int n) {
    definirArray(n);

    std::chrono::high_resolution_clock::time_point t1 = std::chrono::high_resolution_clock::now();
    mergeSort(array, 0, array.size() - 1);
    std::chrono::high_resolution_clock::time_point t2 = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);
    salvarTempo(n, time_span.count());
}