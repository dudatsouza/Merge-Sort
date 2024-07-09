import pandas as pd
import plotly.graph_objects as go
import tkinter as tk
from tkinter import ttk

# Carregar os dados do arquivo CSV
df = pd.read_csv('../../../datasets/outputs/output.csv')

# Obter os diferentes filePath
file_paths = df['filePath'].unique()

# Função para exibir gráfico em uma janela
def exibir_grafico(fig):
    # Criar uma janela Tkinter
    root = tk.Tk()
    root.title("Gráfico de Desempenho")
    
    # Configurar um Canvas do tkinter para exibir o gráfico
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()

    # Converter o gráfico Plotly em um formato que pode ser renderizado no Canvas
    plotly_fig = fig.to_plotly_json()
    tk_fig = go.Figure(plotly_fig)

    # Exibir o gráfico no Canvas do tkinter
    fig_div = tk_fig.to_html(full_html=False, default_height=720, default_width=1280)
    plotly_frame = ttk.Frame(canvas)
    plotly_frame.pack(fill=tk.BOTH, expand=tk.YES)
    plotly_frame.grid(row=0, column=0, sticky=tk.NSEW)
    plotly_frame.columnconfigure(0, weight=1)
    plotly_frame.rowconfigure(0, weight=1)

    # Exibir o gráfico na janela do tkinter
    exibir_grafico(fig)
