# Merge Sort

<div align="center">
  <img align="center" alt="CMake" src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black" />
  <img align="center" height="20px" width="80px" alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white"/>
  <img align="center" height="20px" width="80px" src="https://img.shields.io/badge/VS%20Code-blue?logo=visual%20studio%20code"/>
  <img align="center" height="20px" width="40px" src="https://img.shields.io/badge/c-%2300599C.svg?logo=c&logoColor=white"/>
  <img align="center" height="20px" width="70px" src="https://img.shields.io/badge/c++-%2300599C.svg?logo=c%2B%2B&logoColor=white"/>
  <img align="center" height="20px" width="50px" src="https://img.shields.io/badge/c%23-%23239120.svg?logo=csharp&logoColor=white">
  <img align="center" height="20px" width="60px" src="https://img.shields.io/badge/Java-%23ED8B00.svg?logo=openjdk&logoColor=white"/>
  <img align="center" height="20px" width="80px" src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black"/>
  <img align="center" height="20px" width="50px" src="https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white"/>
  <img align="center" height="20px" width="60px" src="https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=ffdd54"/>
</div>

## Métodos de Ordenação
Métodos de ordenação são algoritmos usados para organizar uma sequência de elementos em uma determinada ordem, geralmente crescente ou decrescente. Esses algoritmos são fundamentais em ciência da computação, pois muitas operações em dados requerem que eles estejam ordenados. 
<br/>**Principais Métodos de Ordenação**
1. Bubble Sort (Ordenação por Bolha)
2. Selection Sort (Ordenação por Seleção)
3. Insertion Sort (Ordenação por Inserção)
4. Merge Sort (Ordenação por Intercalação)
5. Quick Sort (Ordenação Rápida)
6. Heap Sort (Ordenação por Heap)

<br/>**Importância da Ordenação**

1. Eficiência na Pesquisa: Dados ordenados permitem a utilização de algoritmos de busca mais eficientes, como a busca binária, que têm uma complexidade O(log n).
2. Melhoria na Usabilidade: Listas ordenadas são mais fáceis de entender e utilizar, seja para usuários finais ou para outros sistemas que utilizam esses dados.
3. Preparação para Outros Algoritmos: Muitos algoritmos dependem de dados ordenados para funcionarem corretamente ou de maneira mais eficiente, como algoritmos de merge em estruturas de dados e algoritmos de compressão.
4. Agrupamento e Análise: Facilita a detecção de padrões e a realização de análises estatísticas, como a identificação de medianas, percentis, e outras métricas importantes.
<br/>
Assim nota-se que os métodos de ordenação são essenciais para a organização e a eficiência no processamento de dados. Escolher o algoritmo de ordenação adequado para cada situação pode impactar significativamente o desempenho de um sistema, sendo uma decisão crítica no desenvolvimento de software.

## Merge Sort
O Merge Sort é um algoritmo de ordenação que consiste em dividir uma estrutura em subconjuntos e aplicar a ordenação nos elementos extraídos da estrutura original. Após a ordenação desses subconjuntos, é feita a mistura (merge) em um conjunto final ordenado. Podemos dizer literalmente que ele se utiliza daquela boa e velha frase que conhecemos: "Dividir e conquistar".
O que ocorre é o desmembramento do problema em vários subproblemas que são semelhantes ao problema original, mas de menor tamanho, resolvendo esses subproblemas recursivamente e, em seguida, combinando as soluções para criar uma solução para o problema original. Dessa forma ele opera, nos passos principais:
1. **Divisão**: O array original é dividido recursivamente em subarrays menores até que cada subarray contenha apenas um elemento. Isso é feito dividindo repetidamente o array ao meio.

2. **Conquista**: Os subarrays são ordenados recursivamente.

3. **Combinação (Merge)**: Os subarrays ordenados são mesclados para formar subarrays maiores, garantindo que os elementos mesclados estejam em ordem.

A recursão é "finalizada" quando a sequência a ser ordenada atinge o comprimento 1, uma vez que, nessa situação, não há trabalho a ser realizado, uma vez que qualquer sequência com comprimento 1 já se encontra ordenada. 
<br/>
Para entender melhor o funcionamento do Merge Sort, é importante analisar as duas funções principais que compõem o algoritmo: Merge e MergeSort. 

A operação chave do algoritmo de ordenação é a intercalação de duas sequências ordenadas no passo de ``combinação''. Para realizar a intercalação, utilizamos um procedimento auxiliar chamado Merge(A, p, q, r, onde 'A' é o array, 'p' é o índice do primeiro elemento do primeiro subarray, 'q' é o índice do último elemento do primeiro subarray e 'r' é o índice do último elemento do segundo subarray, tais que p ≤ q < r. 

Esse procedimento assume que $A[p..q]$ (subarray esquerdo) e $A[q+1..r]$ (subarray direito) estão ordenados. Ele os mescla para formar um único subarray ordenado que substitui o subarray original $A[p..r]$. O procedimento \texttt{Merge} leva tempo $O(n)$ para mesclar dois subarrays de tamanho $n/2$ cada, onde $n = r - p + 1$ é o número total de elementos a serem mesclados. Em termos computacionais, cada passo básico do procedimento demanda um tempo constante, pois estamos comparando apenas os elementos superiores dos dois subarrays. 
<br/>
**Pseudocódigo:**
```text
Merge(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    Create arrays L[1..n1 + 1] and R[1..n2 + 1]
    
    For i = 1 to n1 do
        L[i] = A[p + i - 1]
    EndFor

    For j = 1 to n2 do
        R[j] = A[q + j]
    EndFor

    L[n1 + 1] = ∞
    R[n2 + 1] = ∞

    i = 1
    j = 1

    For k = p to r do
        If L[i] ≤ R[j] then
            A[k] = L[i]
            i = i + 1
        Else
            A[k] = R[j]
            j = j + 1
        EndIf
    EndFor
```
## Artigo Científico
No trabalho foi realizado um artigo contendo informações mais técnicas e precisas sobre o Merge Sort. Sendo dívidido em Introdução, Metodologia, Modelos de Aplicação e Generalizações, Resultados e Discussões, e a Conclusão. Dessa forma, relatando as informações mais importantes e análises sobre o Merge Sort.

## Implementações 
Para a realização do trabalho foram realizadas implementações em diferentes linguagens de programação. Isto posto, foi implementado o Merge Sort em quatro linguagens compiladas e quatro linguagens interpretadas, sendo essas compiladas C, C++, C# e Rust. Já as Interpetadas Java, JavaScript, PHP e Python. 

## Considerações Finais
O trabalho aborda abrangentemente o Merge Sort, discutindo complexidade de tempo e espaço, modelos de aplicação, generalizações, vantagens e desvantagens. Além de informações sobre as linguagengens de programação abordadas, com os resultados obtidos e comparações de desempenho.  


## Compilação e Execução 

<p align="justify">
Esse programa possui um arquivo Makefile que realiza todo o procedimento de compilação e execução tanto em C quanto em C++. Contudo, há necessidade de uma pequena mudança no arquivo Makefile para variação entre essas linguagens. Para tanto, temos as seguintes diretrizes de execução:
</p>

| Comando                |  Função                                                                                               |                     
| -----------------------| ------------------------------------------------------------------------------------------------------|
|  `make clean`          | Apaga a última compilação realizada contida na pasta build                                            |
|  `make`                | Executa a compilação do programa utilizando o gcc, e o resultado vai para a pasta build               |
|  `make run`            | Executa o programa da pasta build após a realização da compilação                                     |
<p align="right"><a href="#-merge-sort">⬆️ Voltar para ao Início</a></p>
                    
## 🔧 Ambiente de Compilação
A seguir estão os detalhes do ambiente de compilação onde o programa foi executado:

| Componente      | Detalhes                          |
|-----------------|-----------------------------------|
| Sistema Operacional | Ununtu 24.04 LTS |
| Modelo do hardware| Dell Inspiron 13 5330|
| Processador     | Intel Core i7-1360P Processor (18MB Cache, up to 5.00 GHz)|
| Memória RAM     | 16GB 4800MHz LPDDR5 Memory Onboard|
| Armazenamento   | 512GB M.2 PCIe NVMe Solid State Drive|
| Placa de vídeo  | Intel(R) Iris(R) Xe Graphics |
| IDE             | Visual Studio Code 1.63.2|

> [!IMPORTANT]
> Os detalhes acima são baseados no ambiente de compilação utilizado durante o desenvolvimento do programa e podem variar em diferentes sistemas.
<p align="right"><a href="#-merge-sort">⬆️ Voltar para ao Início</a></p>

## 📧 Contato dos Colaboradores
Para mais informações ou sugestões, sinta-se à vontade para entrar em contato:

| Participante           |  Contato  |                     
| -----------------------| ----------|
|  Maíra Lacerda | [![Gmail][Gmail Badge]][Gmail Colab 1] [![Linkedin][Linkedin Badge]][Linkedin Colab 1] [![Instagram][Instagram Badge]][Instagram Colab 1] [![GitHub][GitHub Badge]][GitHub Colab 1]|
|  Maria Eduarda Teixeira | [![Gmail][Gmail Badge]][Gmail Colab 2] [![Linkedin][Linkedin Badge]][Linkedin Colab 2] [![Instagram][Instagram Badge]][Instagram Colab 2] [![GitHub][GitHub Badge]][GitHub Colab 2]|
|  Sergio Ramos | [![Gmail][Gmail Badge]][Gmail Colab 3] [![Linkedin][Linkedin Badge]][Linkedin Colab 3] [![Instagram][Instagram Badge]][Instagram Colab 3] [![GitHub][GitHub Badge]][GitHub Colab 3]          |  

Ficaremos felizes em receber feedbacks, contribuições ou responder a quaisquer dúvidas que você possa ter sobre o programa.
<p align="right"><a href="#-merge-sort">⬆️ Voltar para ao Início</a></p>


[Gmail Badge]: https://img.shields.io/badge/-Gmail-c14438?style=flat-square&logo=Gmail&logoColor=white
[Linkedin Badge]: https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white
[Instagram Badge]: https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white
[GitHub Badge]: https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=GitHub&logoColor=white

[Gmail Colab 1]: mailto:mairaallacerda@gmail.com
[Gmail Colab 2]: mailto:dudateixeirasouza@gmail.com
[Gmail Colab 3]: mailto:sergiohenriquequedasramos@gmail.com

[Linkedin Colab 1]: https://www.linkedin.com/in/ma%C3%ADra-almeida-lacerda
[Linkedin Colab 2]: https://www.linkedin.com/in/maria-eduarda-teixeira-souza-2a2b3a254/
[Linkedin Colab 3]: https://www.linkedin.com/in/sergio-ramos-21057230a

[Instagram Colab 1]: https://www.instagram.com/mairaallacerda/
[Instagram Colab 2]: https://www.instagram.com/dudat_18/
[Instagram Colab 3]: https://www.instagram.com/eu__sergio/

[GitHub Colab 1]: https://github.com/mairaallacerda
[GitHub Colab 2]: https://github.com/dudatsouza
[GitHub Colab 3]: https://github.com/serginnn
