import subprocess

def execute_c(n):
    print("\n\nExecutando código em C...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C/")
    subprocess.run(["./build/app"], input=f"{n}\n../../Entradas/entrada.txt\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C/")

def execute_csharp(n):
    print("\n\nExecutando código em C#...")
    subprocess.run(["dotnet", "run"], input=f"{n}\n../../Entradas/entrada.txt\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C#/")

def execute_cplusplus(n):
    print("\n\nExecutando código em C++...")
    subprocess.run(["make", "clean"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["make"], cwd="../Códigos das Implementações/Código em C++/")
    subprocess.run(["./build/app"], input=f"{n}\n../../Entradas/entrada.txt\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em C++/")

def execute_java(n):
    print("\n\nExecutando código em Java...")
    subprocess.run(["rm", "Main.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["rm", "MergeSortAlgorithm.class"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["javac", "Main.java"], cwd="../Códigos das Implementações/Código em Java/")
    subprocess.run(["java", "Main"], input=f"{n}\n../../Entradas/entrada.txt\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em Java/")

def execute_javascript(n):
    print("\n\nExecutando código em JavaScript...")
    subprocess.run(["node", "main.js", str(n), "../../Entradas/entrada.txt", "../../Saidas/saida.csv"], cwd="../Códigos das Implementações/Código em JavaScript/")

def execute_php(n):
    print("\n\nExecutando código em PHP...")
    subprocess.run(["php", "main.php"], input=f"{n}\n../../Entradas/entrada.txt\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em PHP/")

def execute_python(n):
    print("\n\nExecutando código em Python...")
    subprocess.run(["python3", "main.py"], input=f"{n}\n../../Entradas/entrada.txt\n../../Saidas/saida.csv\n".encode(), cwd="../Códigos das Implementações/Código em Python/")

def executando(n):
    # Execução para C 
    execute_c(n)

    # Execução para C#
    execute_csharp(n)

    # Execução para C++
    execute_cplusplus(n)

    # Execução para Java
    execute_java(n)

    # Execução para JavaScript
    execute_javascript(n)

    # Execução para PHP
    execute_php(n)

    # Execução para Python
    execute_python(n)

def main():
    qntGeracao = int(input("Digite a quantidade de gerações: "))
    repeticoes = int(input("Digite a quantidade vezes irá se repetir para cada gereção: "))
    
    for i in range(qntGeracao):
        print(f"\n\nGerando a {i+1}ª geração...")
        n = int(input("Digite o valor de n: "))
        for j in range(repeticoes):
            print(f"\n\nExecutando a {j+1}ª repetição...")
            executando(n)    

if __name__ == "__main__":
    main()
