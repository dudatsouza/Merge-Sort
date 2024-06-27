import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Carregar os dados do arquivo CSV
df = pd.read_csv('../../datasets/Saidas/saida.csv')

# Obter as diferentes linguagens
linguagens = df['linguagem'].unique()

# Criar um gráfico para cada filePath
for linguagem in linguagens:
    # Filtrar os dados para a linguagem atual
    df_filtered = df[df['linguagem'] == linguagem]

    # Criar o gráfico de linhas
    fig = go.Figure()

    # Adicionar as linhas ao gráfico para cada arquivo de entrada
    file_paths = df_filtered['filePath'].unique()
    for file_path in file_paths:
        df_file_path = df_filtered[df_filtered['filePath'] == file_path]
        fig.add_trace(go.Scatter(
            x=df_file_path['tamanhoArray'], 
            y=df_file_path['tempoExecucao'], 
            mode='lines+markers', 
            name=file_path.split('/')[-1],  # Usar o nome do arquivo como legenda
            marker=dict(size=10)  # Define o tamanho das bolinhas
        ))

    # Adicionar título e nomes dos eixos
    fig.update_layout(
        title={
            'text': f'DESEMPENHO DAS LINGUAGENS - {linguagem}',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'family': 'Courier New', 'size': 30, 'color': 'white'}
        },
        xaxis_title='Tamanho do Array',
        yaxis_title='Tempo de Execução',
        font=dict(
            family="sans-serif",
            size=14,
            color="#7f7f7f"
        ),
        paper_bgcolor="black",
        plot_bgcolor="black",
        legend=dict(
            x=1,
            y=1,
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=12,
                color='white'
            ),
            bgcolor='black',
            bordercolor='black',
            borderwidth=1
        ),
        xaxis=dict(
            gridcolor='rgba(255, 255, 255, 0.2)'  # Cor branca com 20% de opacidade
        ),
        yaxis=dict(
            gridcolor='rgba(255, 255, 255, 0.2)'  # Cor branca com 20% de opacidade
        )
    )

    # Adicionar anotação com legenda abaixo do título
    fig.add_annotation(
        text="Tamanho do Array x Tempo de Execução",
        xref="paper", yref="paper",
        x=0.5, y=1.02,  # Posiciona a anotação acima do gráfico
        showarrow=False,
        font=dict(
            family="Courier New",
            size=18,
            color="rgba(255, 255, 255, 1)"  # Cor da anotação
        ),
        align="center"
    )

    # Exibir o gráfico
    fig.show()

    # Salvar o gráfico como PNG
    file_name = f"../../datasets/Gráficos/Por Linguagem/desempenho_{linguagem}.png"
    pio.write_image(fig, file_name, width=1280, height=720)
    print(f"Gráfico salvo como {file_name}")