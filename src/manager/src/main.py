import subprocess
import os
import time
import sys

def removerAquivosDiretorioEntrada(caminho):
    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

def limparArquivoSaida(caminho):
    with open(caminho, "w") as file:
        file.write("linguagem,tamanhoArray,tempoExecucao,filePath")

def gerarGraficos():
    print("\n-----------------------------")
    print("GERANDO GRÁFICOS\n")
    print("Será gerado 11 gráficos com os resultados obtidos, serão abertos no seu navegador padrão.")
    print("\nDEPOIS DE VISUALIZAR OS GRÁFICOS, FECHAR A JANELA DO NAVEGADOR PARA CONTINUAR A EXECUÇÃO DO PROGRAMA AQUI...")
    print("\nPressione ENTER para continuar...")
    input()
    os.system('python3 ../Gráficos/gráficos.py')
    os.system('python3 ../Gráficos/gráficos2.py')

    print("Gráficos gerados com sucesso, você pode visualizar os gráficos na pasta '../datasets/Gáficos/'.")
    print("-----------------------------")

def abrir_novo_terminal(lock_file_path):
    # Caminho completo do script atual
    caminho_script = "main.py"
    # Comando para abrir um novo terminal e executar este script com o argumento '--no-terminal'
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
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'python3 executador.py'])
    while os.path.exists(lock_file_path):
        time.sleep(1)

    print("\nExecução finalizada com sucesso!")
    print("-----------------------------")

def finalizando():
    print("\n-----------------------------")
    print("FIM DO PROGRAMA\n")
    print("O programa foi finalizado com sucesso!")
    print("-----------------------------")
    print("\nPressione ENTER para sair...")
    input()

           
def main():
    apresentacao()

    removerAquivosDiretorioEntrada("../../datasets/Entradas/")
    limparArquivoSaida("../../datasets/Saidas/saida.csv")
    
    print("EXECUTANDO...\n")
    subprocess.run(["python3", "entradas.py"])

    run()

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

    elif sys.argv[1] == '--no-terminal':
        lock_file_path = sys.argv[2]
        main()

        if os.path.exists(lock_file_path):
            os.remove(lock_file_path)
    print("-----------------------------")

