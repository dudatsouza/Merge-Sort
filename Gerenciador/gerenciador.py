import subprocess
import os

def execute_c(n, file):
    print("\n\nExecutando código em C...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C/")

def execute_csharp(n, file):
    print("\n\nExecutando código em C#...")
    subprocess.run(["dotnet", "run"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C#/")

def execute_cplusplus(n, file):
    print("\n\nExecutando código em C++...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C++/")

def execute_java(n, file):
    print("\n\nExecutando código em Java...")
    subprocess.run(["rm", "Main.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["rm", "MergeSortAlgorithm.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["javac", "Main.java"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["java", "Main"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em Java/")

def execute_javascript(n, file):
    print("\n\nExecutando código em JavaScript...")
    subprocess.run(["node", "main.js", str(n), str(file), "../../Saidas/saida.csv"], cwd="../Códigos das Implementações/Código em JavaScript/")

def execute_php(n, file):
    print("\n\nExecutando código em PHP...")
    subprocess.run(["php", "main.php"], input=f"{n}\n{file}\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em PHP/")

def execute_python(n, file):
    print("\n\nExecutando código em Python...")
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


def main():
    qntGeracao = int(input("Digite a quantidade de gerações: "))
    repeticoes = int(input("Digite a quantidade vezes irá se repetir para cada gereção: "))
    files = list_files_in_directory("../Entradas/")

    for i in range(qntGeracao):
        print(f"\n\nGerando a {i+1}ª geração...")
        n = int(input("Digite o valor de n: "))
        for j in range(repeticoes):
            print(f"\n\nExecutando a {j+1}ª repetição...")
            for file in files:
                arq = "../../Entradas/" + file
                print(f"\n\nExecutando com o arquivo {arq}...")
                executando(n, arq)  
    
    os.system('clear')
    print("\n\nExecução finalizada com sucesso!")

    # gerar gráficos
    os.system('python3 ../Resultados\ e\ Gráficos/gráficos.py')
    os.system('python3 ../Resultados\ e\ Gráficos/gráficos2.py')

if __name__ == "__main__":
    main()
