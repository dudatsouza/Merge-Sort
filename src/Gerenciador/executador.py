import subprocess
import os

def execute_c(n, file):
    print("\nExecutando código em C...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n../../../datasets/Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C/")

def execute_csharp(n, file):
    print("\nExecutando código em C#...")
    subprocess.run(["dotnet", "run"], input=f"{n}\n{file}\n../../../datasets/Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C#/")

def execute_cplusplus(n, file):
    print("\nExecutando código em C++...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n../../../datasets/Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C++/")

def execute_java(n, file):
    print("\nExecutando código em Java...")
    subprocess.run(["rm", "Main.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["rm", "MergeSortAlgorithm.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["javac", "Main.java"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["java", "Main"], input=f"{n}\n{file}\n../../../datasets/Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em Java/")

def execute_javascript(n, file):
    print("\nExecutando código em JavaScript...")
    subprocess.run(["node", "main.js", str(n), str(file), "../../../datasets/Saidas/saida.csv"], cwd="../Códigos das Implementações/Código em JavaScript/")

def execute_php(n, file):
    print("\nExecutando código em PHP...")
    subprocess.run(["php", "main.php"], input=f"{n}\n{file}\n../../../datasets/Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em PHP/")

def execute_python(n, file):
    print("\nExecutando código em Python...")
    subprocess.run(["python3", "main.py"], input=f"{n}\n{file}\n../../../datasets/Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em Python/")

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

def main():
    print("EXECUTANDO CÓDIGOS...")
    files = ["aleatorio.txt", "crescente.txt", "decrescente.txt", "quase_ordenado.txt"]
    for file in files:
        arq = "../../../datasets/Entradas/" + file
        for n in [10, 100, 1000, 10000, 100000, 1000000]:
            print("\n-------------------------")
            print(f"- ARQUIVO {file} com {n} NÚMEROS...")
            executando(n, arq)

if __name__ == "__main__":
    main()
    os.remove("/tmp/executador.lock")