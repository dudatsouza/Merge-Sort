import subprocess
import os
import time
import sys

def removerAquivosDiretorioEntrada(caminho):
    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

def gerarGraficos():
    print("\n-----------------------------")
    print("GERANDO GRÁFICOS\n")
    print("Serão gerado  gráficos com os resultados obtidos e serão abertos no seu navegador padrão.")
    print("\nDEPOIS DE VISUALIZAR OS GRÁFICOS, FECHAR A JANELA DO NAVEGADOR PARA CONTINUAR A EXECUÇÃO DO PROGRAMA AQUI...")
    print("\nPressione ENTER para continuar...")
    input()
    os.system('python3 ../../graphs/src/plot_by_input.py')
    os.system('python3 ../../graphs/src/plot_by_input_type.py')
    os.system('python3 ../../graphs/src/plot_by_language.py')
    os.system('python3 ../../graphs/src/plot_by_language_type.py')

    print("Gráficos gerados com sucesso, você pode visualizar os gráficos na pasta '../../../datasets/graphs/'")
    print("-----------------------------")

def abrir_novo_terminal(lock_file_path):
    caminho_script = "main.py"
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'python3 {caminho_script} --no-terminal {lock_file_path}'])

def apresentacao():
    print("TRABALHO 1 - AEDS I")
    print("\n-----------------------------")
    print("Este trabalho tem como objetivo fazer um estudo do algoritimo Merge Sort. \n\nAqui, é apenas uma das etapas do trabalho, onde será feito a execução de códigos em diferentes linguagens de programação. Inicialmente, será gerado arquivos de entrada para os códigos, e em seguida, será feito a execução dos códigos, por fim, será gerado gráficos com os resultados obtidos. \n\nPara entender melhor o funcionamento do trabalho, leia o README.md.")
    print("-----------------------------")
    enter = input("\nPressione ENTER para continuar...")
    os.system('clear')

def run():
    print("\n-----------------------------")
    print("EXECUTANDO CÓDIGOS\n")
    print("Será aberdo um novo terminal para a execução dos códigos em diferentes linguagens de programação.")
    print("\nISSO PODE DEMORAR BASTANTE, APENAS AGUARDE, SERÁ AVISADO QUANDO ACABAR A EXECUÇÃO...")
    input("\nPressione ENTER para continuar...\n")

    lock_file_path = "/tmp/executador.lock"
    open(lock_file_path, 'w').close()
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'python3 executor.py'])
    while os.path.exists(lock_file_path):
        time.sleep(1)

    print("\nExecução finalizada com sucesso!")
    print("-----------------------------")

def mediaTipoLinguagem():
    print("\n-----------------------------")
    print("CALCULANDO MÉDIA DOS TEMPOS DE EXECUÇÃO\n")
    print("Será calculado a média dos tempos de execução das linguagens compiladas e interpretadas.")
    print("\nPressione ENTER para continuar...")
    input()

    # Ler o arquivo output e salvar os tempos de execução em um dicionário
    with open("../../../datasets/outputs/output.csv", "r") as file:
        # Identificar linguagens compiladas e interpretadas
        lines = file.readlines()
        compiladas = {"C", "C++", "C#", "Rust"}
        interpretadas = {"Java", "JavaScript", "PHP", "Python"}
        times_compiladas = {}
        times_interpretadas = {}

        for line in lines[1:]:  # Pular a primeira linha do cabeçalho
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            lang, size, time, file_path = parts
            key = (int(size), file_path)
            time = float(time)
            if lang in compiladas:
                if key not in times_compiladas:
                    times_compiladas[key] = []
                times_compiladas[key].append(time)
            elif lang in interpretadas:
                if key not in times_interpretadas:
                    times_interpretadas[key] = []
                times_interpretadas[key].append(time)

    # Calcular a média dos tempos de execução e adicionar no final do arquivo
    with open("../../../datasets/outputs/output.csv", "a") as file:
        for key in times_compiladas:
            size, file_path = key
            average_time = sum(times_compiladas[key]) / len(times_compiladas[key])
            lang = "Compiladas"
            average_time = f"{average_time:.10f}"
            file.write(f"{lang},{size},{average_time},{file_path}\n")
        
        for key in times_interpretadas:
            size, file_path = key
            average_time = sum(times_interpretadas[key]) / len(times_interpretadas[key])
            lang = "Interpretadas"
            average_time = f"{average_time:.10f}"
            file.write(f"{lang},{size},{average_time},{file_path}\n")

    print("\nMédias calculadas com sucesso!")
    print("-----------------------------")

def agradecimentoDados():
    print("\n-----------------------------")
    print("Agradecemos a ateção e a execução do programa. Nós nos vemos na próxima!!\n\n")
    print("-----------------------------")
    print("Feito por: - Maíra Lacerda")
    print("           - Maria Eduarda Teixeira")
    print("           - Sergio Henrique")
    print("Engenhaia de Computação - 2024/1 - CEFET/MG - Campus V")
    print("Disciplina: Algoritimos e Estrutura de Dados I")
    print("Professora: Michel Pires")
    print("Acesse o repositório do projeto: https://github.com/dudatsouza/Merge-Sort")

def finalizando():
    print("\n-----------------------------")
    print("FIM DO PROGRAMA\n")
    print("O programa foi finalizado com sucesso!")
    print("-----------------------------")
    print("\nPressione ENTER para finalizar...")
    input()
    os.system('clear')
    agradecimentoDados()
    input("\nPressione ENTER para sair...")

           
def main():
    apresentacao()

    removerAquivosDiretorioEntrada("../../../datasets/inputs")

    print("EXECUTANDO...\n")
    subprocess.run(["python3", "inputs.py"])

    run()
    
    mediaTipoLinguagem()

    gerarGraficos()

    finalizando()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        lock_file_path = "/tmp/main.lock"
        open(lock_file_path, 'w').close()
        print("\n-----------------------------")
        print("TRABALHO 1 - AEDS I")
        print("\nDê ENTER para iniciar a execução que abrirá um novo terminal...")
        input()

        abrir_novo_terminal(lock_file_path)

        while os.path.exists(lock_file_path):
            time.sleep(1)

        print("\nExecução finalizada!")
        agradecimentoDados()

    elif sys.argv[1] == '--no-terminal':
        lock_file_path = sys.argv[2]
        main()

        if os.path.exists(lock_file_path):
            os.remove(lock_file_path)
    print("-----------------------------")

