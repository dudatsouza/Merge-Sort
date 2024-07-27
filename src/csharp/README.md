# 💻 Implementação em C#

<div align="center">
   <img align="center" height="20px" width="80px" alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white"/>
   <img align="center" height="20px" width="80px" src="https://img.shields.io/badge/VS%20Code-blue?logo=visual%20studio%20code"/>
   <img align="center" height="20px" width="80px" src="https://img.shields.io/badge/.NET-5C2D91?logo=.net&logoColor=white"/>
   <img align="center" height="20px" width="50px" src="https://img.shields.io/badge/c%23-%23239120.svg?logo=csharp&logoColor=white">
</div>

## 
Aqui está a implementação do algoritmo Merge Sort em C#. Para entender melhor sobre este projeto, leia o [README.md](../../README.md) principal.

## 🗂 Arquivos

- `src/MergeSort.cs`: Implementação do algoritmo Merge Sort em C#.
- `src/Program.cs`: Programa principal que executa o algoritmo Merge Sort.
- `src/MergeSort.csproj`: Arquivo de configuração do projeto C#.


## 📚 Como Usar
Antes de executar é necessário clonar o repositório. Para isso, siga os passos abaixo:
```bash
git clone https://github.com/dudatsouza/Merge-Sort.git
```

Existe duas maneiras para executar este programa:
1. Através do terminal, onde é compilado e executado o programa, e exibido o resultado no terminal.
2. Através do script executável `../manager/main.py`, neste é executado o programa e gerado o gráfico de desempenho.

### 1. Através do terminal
Para compilar e executar o programa através do terminal, siga os passos abaixo:

1. Abra seu terminal e navegue até o diretório `src/csharp`:
    ```bash
    cd src/csarp
    ```
2. Execute o comando `dotnet run` para compilar e executar o programa:
    ```bash
    dotnet run
    ```
> [!CAUTION]
> Caso não tenha o dotnet instalado, instale-o através do comando:
> ```bash
> sudo apt install dotnet-sdk-5.0
> ```

3. O programa será executado e o resultado será exibido no terminal.
<p align="right"><a href="#-implementação-em-c">⬆️ Voltar para ao Início</a></p>

### 2. Através do script executável
Para compilar e executar o programa através do script executável, siga os passos abaixo:

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
<p align="right"><a href="#-implementação-em-c">⬆️ Voltar para ao Início</a></p>

## 📊 Implementação
Foi implementado o algoritmo Merge Sort de acordo com o pseudocódigo que está no [README.md](../../README.md) principal. Foram feitas algumas modificações para que o algoritmo pudesse ser executado em C#. Veja abaixo algumas informações sobre a implementação:

- **Bibliotecas**: Foram utilizadas as bibliotecas `System`, para funções básicas, `System.Collections.Generic`, para a utilização de listas, `System.Globalization`, para a utilização de formatação de números e `System.IO`, para a manipulação de arquivos.

- **Funções**: A implementação em C# foi feita utilizando orientação a objetos. Tendo as seguintes funções: 
    - `Merge`: Função que faz a junção dos vetores ordenados.
    - `MergeSort`: Função que faz a divisão do vetor em subvetores.
    - `DefinirArray`: Função que define o vetor a ser ordenado.
    - `SalvarTempo`: Função que salva o tempo de execução do algoritmo em um arquivo `.csv`.
    - `Run`: Função que executa o algoritmo.

- **Entrada**: O programa exige que entre com 3 valores: o tamanho do vetor, o nome do arquivo de entrada e o nome do arquivo de saída. O arquivo de entrada deve estar no formato `.txt` e deve conter os valores do vetor separados por espaço, o arquivo de saída será um arquivo `.csv` que conterá o tempo de execução do algoritmo e o tamanho do vetor, que será até qual posição o vetor será ordenado.

- **Saída**: O programa apenas guarda o tempo de execução do algoritmo em um arquivo `.csv` em `../../datasets/outputs/output.csv`. Além de exibir o tempo de execução no terminal. Depois é gerado alguns gráficos de desempenho.

## 📈 Resultados
Os resultados do desempenho do algoritmo da linguagem C#, foram discutidos no artigo do projeto. Para mais informações, acesse o nosso [artigo](../../artigo/Artigo.pdf) ou o [README.md](../../README.md) principal.
<p align="right"><a href="#-implementação-em-c">⬆️ Voltar para ao Início</a></p>

## ⛏ Dotnet

O DOTNET é uma plataforma de desenvolvimento livre e multiplataforma para a construção de aplicativos modernos, incluindo aplicativos Web, aplicativos de IoT e back-ends de API usando C#.


| Comando      | **Descrição**                           |
|--------------|-----------------------------------------|
| `dotnet new console -n MergeSort` | Cria um novo projeto de console chamado `MergeSort` |
| `dotnet run` | Compila e executa o projeto atual |
| `dotnet build` | Compila o projeto atual |
| `dotnet clean` | Remove os arquivos compilados e temporários |
<p align="right"><a href="#-implementação-em-c">⬆️ Voltar para ao Início</a></p>

## 🔧 Ambiente de Compilação
A seguir estão os detalhes do ambiente de compilação onde o programa foi executado:

| Componente      | Detalhes                          |
|-----------------|-----------------------------------|
| Sistema Operacional | Ubuntu 24.04 LTS|
| Modelo do hardware| Dell Inspiron 13 5330|
| Processador     | Intel Core i7-1360P Processor (18MB Cache, up to 5.00 GHz)|
| Memória RAM     | 16GB 4800MHz LPDDR5 Memory Onboard|
| Armazenamento   | 512GB M.2 PCIe NVMe Solid State Drive|
| Placa de vídeo  | Intel(R) Iris(R) Xe Graphics |
| IDE             | Visual Studio Code 1.63.2|

> [!IMPORTANT]
> Os detalhes acima são baseados no ambiente de compilação utilizado durante o desenvolvimento do programa e podem variar em diferentes sistemas.
<p align="right"><a href="#-implementação-em-c">⬆️ Voltar para ao Início</a></p>

## 📧 Contato dos Colaboradores
Para mais informações ou sugestões, sinta-se à vontade para entrar em contato:

| Participante           |  Contato  |                     
| -----------------------| ----------|
|  Maíra Lacerda | [![Gmail][Gmail Badge]][Gmail Colab 1] [![Linkedin][Linkedin Badge]][Linkedin Colab 1] [![Instagram][Instagram Badge]][Instagram Colab 1] [![GitHub][GitHub Badge]][GitHub Colab 1]|
|  Maria Eduarda Teixeira | [![Gmail][Gmail Badge]][Gmail Colab 2] [![Linkedin][Linkedin Badge]][Linkedin Colab 2] [![Instagram][Instagram Badge]][Instagram Colab 2] [![GitHub][GitHub Badge]][GitHub Colab 2]|
|  Sergio Ramos | [![Gmail][Gmail Badge]][Gmail Colab 3] [![Linkedin][Linkedin Badge]][Linkedin Colab 3] [![Instagram][Instagram Badge]][Instagram Colab 3] [![GitHub][GitHub Badge]][GitHub Colab 3]          |  

Ficaremos felizes em receber feedbacks, contribuições ou responder a quaisquer dúvidas que você possa ter sobre o programa.
<p align="right"><a href="#-implementação-em-c">⬆️ Voltar para ao Início</a></p>


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