import pandas as pd

def calculos(df, linguagem1, linguagem2, arqA, n):
    # Filtra os dados para as linguagens e tamanhos de array específicos
    df_linguagem1 = df[(df['linguagem'] == linguagem1) & (df['tamanhoArray'] == n) & (df['filePath'] == arqA)]
    df_linguagem2 = df[(df['linguagem'] == linguagem2) & (df['tamanhoArray'] == n) & (df['filePath'] == arqA)]
    
    if df_linguagem1.empty or df_linguagem2.empty:
        return None

    # Calcula a porcentagem
    tempo1 = df_linguagem1['tempoExecucao'].values[0]
    tempo2 = df_linguagem2['tempoExecucao'].values[0]
    porcentagem = (tempo1 - tempo2) / tempo2 * 100

    # Adicionar prints para depuração
    print(f'{linguagem1} tempo: {tempo1}, {linguagem2} tempo: {tempo2}, porcentagem: {porcentagem}')

    with open('datasets/outputs/porcentagem.csv', 'a') as arqSaida:
        arqSaida.write(f'{linguagem1},{tempo1},{n},{arqA},{linguagem2},{tempo2},{n},{arqA},{porcentagem}\n')

def main():
    df = pd.read_csv('datasets/outputs/output.csv')

    with open('datasets/outputs/porcentagem.csv', 'w') as arqSaida:
        arqSaida.write('linguagem1,tempo1,tamanhoArray,filePath,linguagem2,tempo2,tamanhoArray,filePath,porcentagem\n')
    
    linguagens = [['C', 'Rust', 'Python'], ['C++', 'Rust', 'Python', 'C'], ['C#', 'Rust', 'Python', 'Java'], 
                  ['Rust', 'Python'], ['Java', 'Rust', 'Python'], ['JavaScript', 'Rust', 'Python', 'Java'], ['PHP', 'Rust', 'Python']]
    
    file_paths = df['filePath'].unique()
    n = df['tamanhoArray'].unique()      

    for file_path in file_paths:
        for linguagem in linguagens:
            for i in n:
                if len(linguagem) == 2:
                    calculos(df, linguagem[0], linguagem[1], file_path, i)
                if len(linguagem) == 3:
                    calculos(df, linguagem[0], linguagem[1], file_path, i)
                    calculos(df, linguagem[0], linguagem[2], file_path, i)
                if len(linguagem) == 4:
                    calculos(df, linguagem[0], linguagem[1], file_path, i)
                    calculos(df, linguagem[0], linguagem[2], file_path, i)
                    calculos(df, linguagem[0], linguagem[3], file_path, i)  

def mediaPorcentagem(arqSaida):
    df = pd.read_csv(arqSaida)

    # Cria um dicionário para armazenar as médias
    medias = {}

    for i in range(len(df)):
        linha = df.iloc[i]
        linguagem1 = linha['linguagem1']
        linguagem2 = linha['linguagem2']
        porcentagem = linha['porcentagem']

        if (linguagem1, linguagem2) in medias:
            medias[(linguagem1, linguagem2)].append(porcentagem)
        else:
            medias[(linguagem1, linguagem2)] = [porcentagem]

    # Calcula a média
    mediasPorcentagem = {}
    for key in medias:
        mediasPorcentagem[key] = sum(medias[key]) / len(medias[key])

    # Salva as médias no arquivo de saída
    with open('datasets/outputs/mediaPorcentagem.csv', 'w') as arqSaida:
        arqSaida.write('linguagem1,linguagem2,mediaPorcentagem\n')
        for key in mediasPorcentagem:
            arqSaida.write(f'{key[0]},{key[1]},{mediasPorcentagem[key]:.2f}\n')

if __name__ == '__main__':
    main()
    mediaPorcentagem('datasets/outputs/porcentagem.csv')
