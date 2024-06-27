// IMPLEMENTAÇÃO MERGE SORT EM C++
#include "MergeSort.hpp"

int main() {
    std::cout << "Digite o tamanho do vetor: ";
    int n;
    std::cin >> n;

    std::cout << "Digite o nome do arquivo de entrada: ";
    std::string arqE;
    std::cin >> arqE;

    std::cout << "Digite o nome do arquivo de saída: ";
    std::string arqS;
    std::cin >> arqS;

    MergeSort sorter(arqE, arqS);
    sorter.run(n);

    std::cout << "Execução em C++ finalizada." << std::endl;
    return 0;
}
