// IMPLEMENTAÇÃO MERGE SORT EM C++
#ifndef MERGESORT_HPP
#define MERGESORT_HPP

#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip> 
#include <string> 

class MergeSort {
private:
    std::vector<int> array;
    std::string arq;
    std::string arq2;

    void merge(std::vector<int>& v, int inicio, int meio, int fim);
    void mergeSort(std::vector<int>& v, int inicio, int fim);
    void definirArray(int n);
    void salvarTempo(int n, double timeTaken);

public:
    MergeSort(std::string &arqE, std::string &arqS);
    void run(int n);
};

#endif // MERGESORT_HPP