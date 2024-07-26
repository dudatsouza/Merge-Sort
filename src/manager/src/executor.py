import subprocess
import os
import time

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

# def execute_pascal(n, file, file_output):
#     print("\nExecutando código em Pascal...")
#     subprocess.run(["rm", "main", "main.o", "MergeSort.o", "MergeSort.ppu"], cwd="../../pascal/src")
#     subprocess.run(["fpc", "main.pas"], cwd="../../pascal/src")
#     subprocess.run(["./main"], input=f"{n}\n{file}\n{file_output}\n".encode(), cwd="../../pascal/src")

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

def executando(n, file):
    file_output = "../../../datasets/outputs/temp.csv"
    # Execução para C 
    execute_c(n, file, file_output)

    # Execução para C++
    execute_cplusplus(n, file, file_output)

    # Execução para Rust
    execute_rust(n, file, file_output)

    # Execução para Pascal
    # execute_pascal(n, file, file_output)
    
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

def calcular_media(file_temp, file_output):
    with open(file_temp, "r") as file:
        lines = file.readlines()
        times = {}

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            lang, size, time, file_path = parts
            key = (lang, int(size), file_path)
            if key not in times:
                times[key] = []
            times[key].append(float(time))
    
    with open(file_output, "w") as file:
        file.write("linguagem,tamanhoArray,tempoExecucao,filePath\n")
        for key in times:
            lang, size, file_path = key
            # no file_path tem o caminho completo, então vamos pegar só o nome do arquivo
            file_path = file_path.split("/")[-1]
            average_time = sum(times[key]) / len(times[key])
            # garantindo q o tempo de execução seja um número com 10 casas decimais
            average_time = f"{average_time:.10f}"
            file.write(f"{lang},{size},{average_time},{file_path}\n")

def main():
    print("EXECUTANDO CÓDIGOS...")
    files = ["random1.txt", 
             "random2.txt", 
             "random3.txt", 
             "ascending.txt", 
             "descending.txt", 
             "nearly_sorted_ascending.txt", 
             "nearly_sorted_descending.txt"]
    file_output = "../../../datasets/outputs/output.csv"
    file_temp = "../../../datasets/outputs/temp.csv"
    subprocess.run(["rm", file_temp, file_output])

    inicio = time.time()
    for file in files:
        arq = "../../../datasets/inputs/" + file
        for n in [100, 1000, 10000, 100000, 500000, 1000000]:
            print("\n-------------------------")
            print(f"- ARQUIVO {file} com {n} NÚMEROS...")
            for i in range(10):
                executando(n, arq)
    fim = time.time()

    print(f"Tempo de execução: {fim - inicio:.10f}")
    calcular_media(file_temp, file_output)
    subprocess.run(["rm", file_temp])


if __name__ == "__main__":
    main()
    os.remove("/tmp/executador.lock")