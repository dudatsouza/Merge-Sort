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

### Gerar Gráficos


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
    **- OBSERVAÇÃO:** Caso não tenha o Python ou a biblioteca Matplotlib instalada, instale-os através dos comandos:
    ```bash
    sudo apt install python3
    pip install matplotlib
    ```

3. Os gráficos de desempenho serão gerados e salvos no diretório `datasets/graphs/`.

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
    **- OBSERVAÇÃO:** Caso não tenha o python instalado, instale-o através do comando:
    ```bash
    sudo apt install python3
    ```
3. O programa será executado e o gráfico de desempenho será gerado.

## 📊 Gráficos

Os gráficos de desempenho dos algoritmos de ordenação são gerados e será abera uma janela no seu navegador com os gráficos. Além disso, os gráficos são salvos no diretório `datasets/graphs/`. Serão gerados dois tipos de gráficos:
1. **Por Entrada:** Gráfico de desempenho dos algoritmos para cada entrada. Estarão na pasta `datasets/graphs/by_input/`.
2. **Por Algoritmo:** Gráfico de desempenho dos algoritmos para cada algoritmo. Estarão na pasta `datasets/graphs/by_algorithm/`.

## 📧 Contato

Para mais informações ou sugestões, sinta-se à vontade para entrar em contato:

- ✉️ **E-mail**: [![Gmail Badge](https://img.shields.io/badge/-dudateixeirasouza@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:dudateixeirasouza@gmail.com)](mailto:dudateixeirasouza@gmail.com)
- 💼 **LinkedIn**: [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/maria-eduarda-teixeira-souza-2a2b3a254/)
- 📸 **Instagram**: [![Instagram Badge](https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white)](https://www.instagram.com/dudat_18/)

Ficarei feliz em receber feedbacks, contribuições ou responder a quaisquer dúvidas que você possa ter sobre o programa.
