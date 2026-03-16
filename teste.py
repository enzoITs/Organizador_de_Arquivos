import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def selecionar_pasta():
    # Abre o seletor de diretórios
    caminho_string = filedialog.askdirectory()
    
    if caminho_string:
        # Converte a string para um objeto Path
        pasta_selecionada = Path(caminho_string)
        
        # Agora você pode usar métodos do pathlib, como .parts, .name, .exists(), etc.
        print(f"Caminho selecionado: {pasta_selecionada}")
        print(f"Nome da pasta: {pasta_selecionada.name}")
        
        # Atualiza o label na interface para mostrar que funcionou
        label_status.config(text=f"Pasta: {pasta_selecionada.name}")
        
        return pasta_selecionada

# Configuração básica da janela Tkinter
root = tk.Tk()
root.title("Selecionador de Pastas")
root.geometry("400x200")

# Elementos da Interface
label_instrucao = tk.Label(root, text="Clique no botão para escolher um diretório:")
label_instrucao.pack(pady=20)

botao_selecionar = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack()

label_status = tk.Label(root, text="Nenhuma pasta selecionada", fg="blue")
label_status.pack(pady=20)

root.mainloop()