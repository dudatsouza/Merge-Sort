// IMPLEMENTAÇÃO MERGE SORT EM C++
#ifndef MERGESORTALGORITHM_HPP
#define MERGESORTALGORITHM_HPP

#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip>  

using namespace std;
using namespace chrono;

class MergeSortAlgorithm {
private:
    vector<int> array;
    string arq;
    string arq2;

    void merge(vector<int>& v, int inicio, int meio, int fim);
    void mergeSort(vector<int>& v, int inicio, int fim);
    void definirArray(int n);
    void salvarTempo(int n, double timeTaken);

public:
    MergeSortAlgorithm(const string &arqE, const string &arqS);
    void run(int n);
};

#endif // MERGESORTALGORITHM_HPP
