# 💻 Implementação em C

<div align="center">
    <img align="center" height="20px" width="80px" alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white"/>
    <img align="center" height="20px" width="80px" src="https://img.shields.io/badge/VS%20Code-blue?logo=visual%20studio%20code"/>
    <img align="center" height="20px" width="80px" src="https://img.shields.io/badge/MakeFile-green?logo=make">
    <img align="center" height="20px" width="40px" src="https://img.shields.io/badge/c-%2300599C.svg?logo=c&logoColor=white"/>
</div>

## 
Aqui está a implementação do algoritmo Merge Sort em C. Para entender melhor sobre este projeto, leia o [README.md](../../README.md) principal.

## 🗂 Arquivos

- `src/merge_sort.c`: Implementação do algoritmo Merge Sort em C.
- `src/merge_sort.h`: Declaração das funções do algoritmo Merge Sort.
- `src/main.c`: Programa principal que executa o algoritmo Merge Sort.
- `makefile`: Script de construção para compilar o código.

## 📚 Como Usar
Existe duas maneiras para executar este programa:
1. Através do terminal, utilizando o Makefile.
2. Através do script executável `../manager/main.py`, neste é executado o programa e gerado o gráfico de desempenho.

### 1. Através do terminal
Para compilar e executar o programa através do terminal, siga os passos abaixo:

1. Abra seu terminal e navegue até o diretório `src/c`:
    ```bash
    cd src/c
    ```
2. Execute o comando `make clean` para remover os arquivos compilados:
    ```bash
    make clean
    ```
3. Execute o comando `make` para compilar o programa:
    ```bash
    make
    ```
4. Execute o comando `make run` para executar o programa:
    ```bash
    make run
    ```
5. O programa será executado e o resultado será exibido no terminal.

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
    **- OBSERVAÇÃO:** Caso não tenha o python instalado, instale-o através do comando:
    ```bash
    sudo apt install python3
    ```
3. O programa será executado e o gráfico de desempenho será gerado.

## ⛏ Makefile

O Makefile é um utilitário que automatiza o processo de compilação e execução de programas. Aqui estão os principais comandos do Makefile para este projeto:

| Comando      | **Descrição**                           |
|--------------|-----------------------------------------|
| `make`       | Compila o programa.                     |
| `make run`   | Executa o programa com o arquivo de entrada fornecido. |
| `make clean` | Remove os arquivos compilados.          |

## 📧 Contato

Para mais informações ou sugestões, sinta-se à vontade para entrar em contato:

- ✉️ **E-mail**: [![Gmail Badge](https://img.shields.io/badge/-dudateixeirasouza@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:dudateixeirasouza@gmail.com)](mailto:dudateixeirasouza@gmail.com)
- 💼 **LinkedIn**: [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/maria-eduarda-teixeira-souza-2a2b3a254/)
- 📸 **Instagram**: [![Instagram Badge](https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white)](https://www.instagram.com/dudat_18/)

Ficarei feliz em receber feedbacks, contribuições ou responder a quaisquer dúvidas que você possa ter sobre o programa. 
