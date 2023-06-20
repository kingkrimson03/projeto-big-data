import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk

# Função para exibir informações da coluna
def exibir_informacoes(coluna):
    # Lendo o arquivo CSV
    tabela = pd.read_csv("dados.csv", sep=";")

    # Verificando se a coluna existe
    if coluna in tabela.columns:
        coluna_data = tabela[coluna]

        # Exibindo informações da coluna
        info = f"Informações da coluna '{coluna}':\n"
        info += f"Total de valores: {len(coluna_data)}\n"
        info += f"Valor mínimo: {coluna_data.min()}\n"
        info += f"Valor máximo: {coluna_data.max()}\n"
        info += f"Média: {coluna_data.mean()}\n"
        info += f"Desvio padrão: {coluna_data.std()}\n"

        # Exibindo informações em uma nova janela
        info_window = tk.Toplevel(window)
        info_window.title("Informações da Coluna")
        label = tk.Label(info_window, text=info, padx=10, pady=10)
        label.pack()
    else:
        print("Coluna não encontrada.")

# Criação da interface gráfica
window = tk.Tk()
window.title("Programeixons")

# Carregar a imagem de fundo
imagem_fundo = Image.open("imagem.jpeg")
imagem_fundo = imagem_fundo.resize((800, 600), Image.ANTIALIAS)  # Redimensionar a imagem para ajustar à janela
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

# Exibir a imagem de fundo
label_fundo = tk.Label(window, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Componentes da interface
label = tk.Label(window, text="Digite o nome da coluna:")
label.pack()

entry = tk.Entry(window)
entry.pack()

def handle_button_click():
    coluna = entry.get()
    exibir_informacoes(coluna)

button = tk.Button(window, text="Exibir Informações", command=handle_button_click)
button.pack()

# Execução da interface gráfica
window.mainloop()