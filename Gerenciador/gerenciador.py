import subprocess
import os

def execute_c(n, file):
    print("\nExecutando código em C...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C/")

def execute_csharp(n, file):
    print("\nExecutando código em C#...")
    subprocess.run(["dotnet", "run"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C#/")

def execute_cplusplus(n, file):
    print("\nExecutando código em C++...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C++/")

def execute_java(n, file):
    print("\nExecutando código em Java...")
    subprocess.run(["rm", "Main.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["rm", "MergeSortAlgorithm.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["javac", "Main.java"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["java", "Main"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em Java/")

def execute_javascript(n, file):
    print("\nExecutando código em JavaScript...")
    subprocess.run(["node", "main.js", str(n), str(file), "../../Saidas/saida.csv"], cwd="../Códigos das Implementações/Código em JavaScript/")

def execute_php(n, file):
    print("\nExecutando código em PHP...")
    subprocess.run(["php", "main.php"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em PHP/")

def execute_python(n, file):
    print("\nExecutando código em Python...")
    subprocess.run(["python3", "main.py"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em Python/")

def executando(n, file):
    # Execução para C 
    execute_c(n, file)

    # Execução para C#
    execute_csharp(n, file)

    # Execução para C++
    execute_cplusplus(n, file)

    # Execução para Java
    execute_java(n, file)

    # Execução para JavaScript
    execute_javascript(n, file)

    # Execução para PHP
    execute_php(n, file)

    # Execução para Python
    execute_python(n, file)
    
def list_files_in_directory(directory):
    # Lista para armazenar os nomes dos arquivos
    files_list = []

    # Iterar sobre os itens no diretório
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files_list.append(item)

    return files_list     

def remove_files_in_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

def main():
    # Remover arquivos de entrada
    remove_files_in_directory("../Entradas/datasets/")

    # Remover arquivos de saída
    remove_files_in_directory("../Saidas/")

    # escrever a primeira linha no arquivo de saida ../Saidas/saida.csv
    with open("../Saidas/saida.csv", "w") as file:
        file.write("linguagem,tamanhoArray,tempoExecucao,filePath")
    

    # Gerar arquivos de entrada
    subprocess.run(["python3", "../Entradas/entradas.py"])

    # Armazenar nomes dos arquivos de entrada
    files = list_files_in_directory("../Entradas/datasets/")

    # Executar códigos
    print("Pressione ENTER para executar os códigos...")
    input()
    os.system('clear')
    print("EXECUTANDO CÓDIGOS...")
    for file in files:
        arq = "../../Entradas/datasets/" + file
        print("\n-------------------------")
        print(f"Executando com o arquivo {file}...")
        for n in [10, 100, 1000, 10000, 100000, 1000000]:
            print(f"Executando com n = {n}...")
            executando(n, arq)  
    print("\n--------------------------------------------------")
    
    os.system('clear')
    print("Execução finalizada com sucesso!")
    enter = input("Pressione ENTER para continuar...")
    # gerar gráficos
    os.system('python3 ../Resultados\ e\ Gráficos/gráficos.py')
    os.system('python3 ../Resultados\ e\ Gráficos/gráficos2.py')

if __name__ == "__main__":
    main()