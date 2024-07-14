import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Carregar os dados do arquivo CSV até a linha 336
df = pd.read_csv('../../../datasets/outputs/output.csv')
df = df.iloc[336:]

# Obter os diferentes filePath
file_paths = df['filePath'].unique()
# Criar um gráfico para cada filePath
for file_path in file_paths:
    # Filtrar os dados para o filePath atual
    df_filtered = df[df['filePath'] == file_path]
    # Criar o gráfico de linhas
    fig = go.Figure()
    # Adicionar as linhas ao gráfico para cada linguagem
    linguagens = df_filtered['linguagem'].unique()
    for linguagem in linguagens:
        df_linguagem = df_filtered[df_filtered['linguagem'] == linguagem]
        fig.add_trace(go.Scatter(
            x=df_linguagem['tamanhoArray'], 
            y=df_linguagem['tempoExecucao'], 
            mode='lines+markers', 
            name=linguagem,
            marker=dict(size=10)  # Define o tamanho das bolinhas
        ))
    # Adicionar título e nomes dos eixos
    fig.update_layout(
        title={
            'text': f'DESEMPENHO DAS LINGUAGENS - {file_path.split(".")[0]}',
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
    file_name = f"../../../datasets/graphs/by_input_type/performance_{file_path.split('.')[0]}.png"
    pio.write_image(fig, file_name, format='png', width=1280, height=720)
    print(f"Gráfico salvo como {file_name}")