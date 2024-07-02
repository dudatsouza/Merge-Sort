# 📊 Geração de Gráficos

<div align="center">
   <img align="center" height="20px" width="80px" alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white"/>
   <img align="center" height="20px" width="80px" src="https://img.shields.io/badge/VS%20Code-blue?logo=visual%20studio%20code"/>
   <img align="center" height="20px" width="80px" alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white"/>
   <img align="center" height="20px" width="80px" alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-ffffff?logo=plotly&logoColor=white"/>
</div>

##
Esta pasta contém os scripts necessários para gerar gráficos de desempenho dos algoritmos de ordenação. Para entender melhor sobre este projeto, leia o [README.md](../../README.md) principal.

## 🗂 Arquivos

- `src/plot.py`: Script para plotar gráficos.
- `src/plot_utils.py`: Funções utilitárias para plotagem.

## 📚 Como Usar
Antes de executar é necessário clonar o repositório. Para isso, siga os passos abaixo:
```bash
git clone https://github.com/dudatsouza/Merge-Sort.git
```

Existem duas maneiras para gerar os gráficos de desempenho dos algoritmos de ordenação:

### 1. Através do script de gráficos
1. Abra seu terminal e navegue até o diretório `src/graphs`:
    ```bash
    cd src/graphs
    ```

2. Execute o script de plotagem:
    ```bash
    python3 plot.py
    ```
    Depois faça novamente com o outro script:
    ```bash
    python3 plot_utils.py
    ```
> [!CAUTION]
> Caso não tenha o Python ou a biblioteca Matplotlib instalada, instale-os através dos comandos:
> ```bash
> sudo apt install python3
> pip install matplotlib
> ```

3. Os gráficos de desempenho serão gerados e salvos no diretório `datasets/graphs/`.
<p align="right"><a href="#-geração-de-gráficos">⬆️ Voltar para ao Início</a></p>

### 2. Através do script gerenciador

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
<p align="right"><a href="#-geração-de-gráficos">⬆️ Voltar para ao Início</a></p>

## 📊 Gráficos

Os gráficos de desempenho dos algoritmos de ordenação são gerados e será abera uma janela no seu navegador com os gráficos. Além disso, os gráficos são salvos no diretório `datasets/graphs/`. Serão gerados dois tipos de gráficos:
1. **Por Entrada:** Gráfico de desempenho dos algoritmos para cada entrada. Estarão na pasta `datasets/graphs/by_input/`.
2. **Por Algoritmo:** Gráfico de desempenho dos algoritmos para cada algoritmo. Estarão na pasta `datasets/graphs/by_algorithm/`.
<p align="right"><a href="#-geração-de-gráficos">⬆️ Voltar para ao Início</a></p>

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
<p align="right"><a href="#-geração-de-gráficos">⬆️ Voltar para ao Início</a></p>

## 📧 Contato dos Colaboradores
Para mais informações ou sugestões, sinta-se à vontade para entrar em contato:

| Participante           |  Contato  |                     
| -----------------------| ----------|
|  Maíra Lacerda | [![Gmail][Gmail Badge]][Gmail Colab 1] [![Linkedin][Linkedin Badge]][Linkedin Colab 1] [![Instagram][Instagram Badge]][Instagram Colab 1] [![GitHub][GitHub Badge]][GitHub Colab 1]|
|  Maria Eduarda Teixeira | [![Gmail][Gmail Badge]][Gmail Colab 2] [![Linkedin][Linkedin Badge]][Linkedin Colab 2] [![Instagram][Instagram Badge]][Instagram Colab 2] [![GitHub][GitHub Badge]][GitHub Colab 2]|
|  Sergio Ramos | [![Gmail][Gmail Badge]][Gmail Colab 3] [![Linkedin][Linkedin Badge]][Linkedin Colab 3] [![Instagram][Instagram Badge]][Instagram Colab 3] [![GitHub][GitHub Badge]][GitHub Colab 3]          |  

Ficaremos felizes em receber feedbacks, contribuições ou responder a quaisquer dúvidas que você possa ter sobre o programa.
<p align="right"><a href="#-geração-de-gráficos">⬆️ Voltar para ao Início</a></p>


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