import shutil
from pathlib import Path
from datetime import datetime
import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Sistema de Organização')
app.geometry('500x500')

mapa_extensao = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt"],
    "Planilhas": [".xlsx", ".xls", ".csv", ".ods"],
    "Apresentacoes": [".pptx", ".ppt", ".odp"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Executaveis": [".exe", ".msi", ".bat", ".sh", ".appimage", ".run"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma"],
    "Programacao": [".py", ".js", ".html", ".css", ".json", ".xml", ".cpp", ".c", ".java", ".php"],
    "Fontes": [".ttf", ".otf", ".woff", ".woff2"],
    "ISO_e_Disco": [".iso", ".img", ".vcd"],
    "Design": [".psd", ".ai", ".xd", ".fig", ".cdr"]
}

# registro de log
def registro_log(mensagem):
    data_formatada = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('logs.txt', 'a', encoding='utf-8') as log:
        log.write(f'{data_formatada} | {mensagem} \n')

# organizar os arquivos
def organizar_arquivo():
    contagem_de_movimentos = {}
    local = filedialog.askdirectory()
    pasta_para_organizar = Path(local)

    if not pasta_para_organizar.exists():
        print('Pasta nao existe!')
        return

    for arquivo in pasta_para_organizar.iterdir():
        if not arquivo.is_file():
            continue
        nome_categoria = 'Outros'
        for categoria, extensoes in mapa_extensao.items():
                if arquivo.suffix.lower() in extensoes:
                    nome_categoria = categoria
                    break

        subpasta = pasta_para_organizar / nome_categoria
        subpasta.mkdir(exist_ok=True, parents=True)
        destino = subpasta / arquivo.name
        if destino.exists():
            print("Arquivo já existe")
            continue
        else:
            shutil.move(arquivo, destino)

        registro_log(f'{arquivo} movido para {destino}')

        if nome_categoria in contagem_de_movimentos:
            contagem_de_movimentos[nome_categoria] +=1
        else:
            contagem_de_movimentos[nome_categoria] = 1    
        print(f'Arquivo {arquivo.name} movido para {nome_categoria}')

    for categoria, total in contagem_de_movimentos.items():
        print(f'Foram movidos {total} arquivos para a pasta {categoria}')            

botao_selecionar = ctk.CTkButton(app, text="Selecionar Pasta", command=organizar_arquivo)
botao_selecionar.pack(pady=40)

app.mainloop()
