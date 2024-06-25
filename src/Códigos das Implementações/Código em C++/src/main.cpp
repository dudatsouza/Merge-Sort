// IMPLEMENTAÇÃO MERGE SORT EM C++
#include "MergeSortAlgorithm.hpp"

int main() {
    cout << "Digite o tamanho do vetor: ";
    int n;
    cin >> n;

    cout << "Digite o nome do arquivo de entrada: ";
    string arqE;
    cin >> arqE;

    cout << "Digite o nome do arquivo de saída: ";
    string arqS;
    cin >> arqS;

    MergeSortAlgorithm sorter(arqE, arqS);
    sorter.run(n);

    cout << "Execução em C++ finalizada\n";
    return 0;
}
