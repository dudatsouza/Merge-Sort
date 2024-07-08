import subprocess
import os

def execute_c(n, file, file_output):
    file = file[3:]
    file_output = file_output[3:]
    print("\nExecutando código em C...")
    subprocess.run(["make", "clean"], cwd="../../c/")
    subprocess.run(["make"], cwd="../../c/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../c/")

def execute_cplusplus(n, file, file_output):
    file = file[3:]
    file_output = file_output[3:]
    print("\nExecutando código em C++...")
    subprocess.run(["make", "clean"], cwd="../../cpp/")
    subprocess.run(["make"], cwd="../../cpp/")
    subprocess.run(["./build/app"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../cpp/")

def execute_rust(n, file, file_output):
    file = file[3:]
    file_output = file_output[3:]
    print("\nExecutando código em Rust...")
    subprocess.run(["cargo", "clean"], cwd="../../rust/")
    subprocess.run(["cargo", "build", "--release"], cwd="../../rust/")
    subprocess.run(["./target/release/merge_sort"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../rust/")

def execute_pascal(n, file, file_output):
    print("\nExecutando código em Pascal...")
    subprocess.run(["rm", "main"], cwd="../../pascal/src")
    subprocess.run(["rm", "main.o"], cwd="../../pascal/src")
    subprocess.run(["rm", "MergeSort.o"], cwd="../../pascal/src")
    subprocess.run(["rm", "MergeSort.ppu"], cwd="../../pascal/src")
    subprocess.run(["fpc", "main.pas"], cwd="../../pascal/src")
    subprocess.run(["./main"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../pascal/src")

def execute_csharp(n, file, file_output):
    file = file[3:]
    file_output = file_output[3:]
    print("\nExecutando código em C#...")
    subprocess.run(["dotnet", "run"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../csharp/")

def execute_java(n, file, file_output):
    print("\nExecutando código em Java...")
    subprocess.run(["rm", "Main.class"], cwd="../../java/src")
    subprocess.run(["rm", "MergeSort.class"], cwd="../../java/src")
    subprocess.run(["javac", "Main.java"], cwd="../../java/src")
    subprocess.run(["java", "Main"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../java/src/")

def execute_javascript(n, file, file_output):
    print("\nExecutando código em JavaScript...")
    subprocess.run(["node", "main.js", str(n), str(file), str(file_output)], cwd="../../javascript/src/")

def execute_php(n, file, file_output):
    print("\nExecutando código em PHP...")
    subprocess.run(["php", "main.php"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../php/src/")

def execute_python(n, file, file_output):
    print("\nExecutando código em Python...")
    subprocess.run(["python3", "main.py"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../python/src/")

def executando(n, file, file_output):
    # Execução para C 
    execute_c(n, file, file_output)

    # Execução para C++
    execute_cplusplus(n, file, file_output)

    # Execução para Rust
    execute_rust(n, file, file_output)

    # Execução para Pascal
    execute_pascal(n, file, file_output)

    # Execução para C#
    execute_csharp(n, file, file_output)

    # Execução para Java
    execute_java(n, file, file_output)

    # Execução para JavaScript
    execute_javascript(n, file, file_output)

    # Execução para PHP
    execute_php(n, file, file_output)

    # Execução para Python
    execute_python(n, file, file_output)

def main():
    print("EXECUTANDO CÓDIGOS...")
    files = ["random.txt", "ascending.txt", "descending.txt", "nearly_sorted_ascending.txt", "nearly_sorted_descending.txt"]
    file_output = "../../../datasets/outputs/output.csv"
    for file in files:
        arq = "../../../datasets/inputs/" + file
        for n in [10, 100, 1000, 10000, 100000, 1000000]:
            print("\n-------------------------")
            print(f"- ARQUIVO {file} com {n} NÚMEROS...")
            executando(n, arq, file_output)

if __name__ == "__main__":
    main()
    os.remove("/tmp/executador.lock")