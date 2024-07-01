# 📂 Diretório SRC

<div align="center">
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

##
Este diretório contém as implementações do algoritmo Merge Sort em várias linguagens de programação, bem como scripts para gerenciar a execução dos algoritmos e gerar gráficos de desempenho. Para entender melhor sobre este projeto, leia o [README.md](../README.md) principal.

## 📁 Estrutura das Pastas

Veja abaixo a estrutura de pastas e arquivos deste diretório:
- `c/`: Implementação em C.
- `csharp/`: Implementação em C#.
- `cpp/`: Implementação em C++.
- `java/`: Implementação em Java.
- `javascript/`: Implementação em JavaScript.
- `php/`: Implementação em PHP.
- `python/`: Implementação em Python.
- `manager/`: Scripts para gerenciar a execução dos algoritmos.
- `graphs/`: Scripts para gerar gráficos de desempenho.


    ```
    │
    ├── src/
    │   ├── c/
    │   │   ├── build/
    │   │   ├── src/
    │   │   │   └── merge_sort.c
    │   │   ├── makefile
    |   |   └── README.md
    |   |
    │   ├── csharp/
    │   │   ├── bin/
    │   │   ├── obj/
    │   │   ├── src/
    │   │   │   ├── MergeSort.cs
    │   │   │   └── Program.cs
    │   │   └── MergeSort.csproj
    |   |   └── README.md
    |   |
    │   ├── cpp/
    │   │   ├── build/
    │   │   ├── src/
    │   │   │   ├── main.cpp
    │   │   │   └── MergeSort.cpp
    │   │   ├── makefile
    |   |   └── README.md
    |   |
    │   ├── java/
    │   │   ├── src/
    │   │   │   ├── Main.java
    │   │   │   └── MergeSort.java
    |   |   └── README.md
    |   |
    │   ├── javascript/
    │   │   ├── src/
    │   │   │   ├── main.js
    │   │   │   └── MergeSort.js
    |   |   └── README.md
    |   |
    │   ├── php/
    │   │   ├── src/
    │   │   │   ├── main.php
    │   │   │   └── MergeSort.php
    |   |   └── README.md
    |   |
    │   ├── python/
    │   │   ├── src/
    │   │   │   ├── main.py
    │   │   │   └── MergeSort.py
    |   |   └── README.md
    |   |
    │   ├── manager/
    │   │   ├── src/
    │   │   │   ├── inputs.py
    │   │   │   ├── executor.py
    │   │   │   └── main.py
    |   |   └── README.md
    |   |
    │   └── graphs/
    │       ├── src/
    │       │   ├── plot.py
    │       │   └── plot_utils.py
    |       └── README.md
    │
    └── README.md
    ```

## 📚 Como Usar

Cada subdiretório contém um README específico com instruções detalhadas sobre como compilar e executar o código na linguagem correspondente. Primeiramente clone o repósitório depois siga as seguintes intruções:

```bash
git clone https://github.com/dudatsouza/Merge-Sort.git
```


### ⛏ Compilação e Execução
***
Para compilar e executar as implementações, navegue até o subdiretório desejado e siga as instruções no README correspondente.

### 📊 Gerenciamento de Execução e Geração de Gráficos
***
Para usar o gerenciador de execução e gerar gráficos de desempenho:
1. Abra seu terminal e navegue até o diretório `src/manager`:
    ```bash
    cd src/manager
    ```
2. Execute o script em python:
    ```bash
    python3 main.py
    ```
> [!CAUTION]
> Caso não tenha o python instalado, instale-o através do comando:
> ```bash
> sudo apt install python3
> ```
3. O programa será executado e o gráfico de desempenho será gerado.

## 🔧 Ambiente de Compilação
A seguir estão os detalhes do ambiente de compilação onde o programa foi executado:

| Componente      | Detalhes                          |
|-----------------|-----------------------------------|
| Sistema Operacional | Ununtu 22.04.4 LTS  - 64 bits|
| Modelo do hardware| Dell Inspiron 13 5330|
| Processador     | Intel Core i7-1360P Processor (18MB Cache, up to 5.00 GHz)|
| Memória RAM     | 16GB 4800MHz LPDDR5 Memory Onboard|
| Armazenamento   | 512GB M.2 PCIe NVMe Solid State Drive|
| Placa de vídeo  | Intel(R) Iris(R) Xe Graphics |
| IDE             | Visual Studio Code 1.63.2|

> [!IMPORTANT]
> Os detalhes acima são baseados no ambiente de compilação utilizado durante o desenvolvimento do programa e podem variar em diferentes sistemas.
<p align="right"><a href="#-diretório-src">⬆️ Voltar para ao Início</a></p>

## 📧 Contato dos Colaboradores
Para mais informações ou sugestões, sinta-se à vontade para entrar em contato:

| Participante           |  Contato  |                     
| -----------------------| ----------|
|  Maíra Lacerda | [![Gmail][Gmail Badge]][Gmail Colab 1] [![Linkedin][Linkedin Badge]][Linkedin Colab 1] [![Instagram][Instagram Badge]][Instagram Colab 1] [![GitHub][GitHub Badge]][GitHub Colab 1]|
|  Maria Eduarda Teixeira | [![Gmail][Gmail Badge]][Gmail Colab 2] [![Linkedin][Linkedin Badge]][Linkedin Colab 2] [![Instagram][Instagram Badge]][Instagram Colab 2] [![GitHub][GitHub Badge]][GitHub Colab 2]|
|  Sergio Ramos | [![Gmail][Gmail Badge]][Gmail Colab 3] [![Linkedin][Linkedin Badge]][Linkedin Colab 3] [![Instagram][Instagram Badge]][Instagram Colab 3] [![GitHub][GitHub Badge]][GitHub Colab 3]          |  

Ficaremos felizes em receber feedbacks, contribuições ou responder a quaisquer dúvidas que você possa ter sobre o programa.

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