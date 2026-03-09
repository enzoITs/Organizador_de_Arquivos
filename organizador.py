import shutil
from pathlib import Path
from datetime import datetime

mapa_extensao = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Executaveis": [".exe", ".msi", ".sh"],
}

# extrair o arquivo zip
def descompactar_arquivo(arquivo_zip, pasta_organizada):
    diretorio_organizado = Path(pasta_organizada)
    zip_desorganizado = Path(arquivo_zip)
    if not zip_desorganizado.exists():
        print('Arquivo Zip não existe!')
        return
    print(f'Extraindo o arquivo {zip_desorganizado}')
    if not diretorio_organizado.exists():
        diretorio_organizado.mkdir()
    shutil.unpack_archive(zip_desorganizado, diretorio_organizado)

# organizar os arquivos
def organizar_arquivo(organizador):
    contagem_de_movimentos = {}
    pasta_para_organizar = Path(organizador)
    
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

        if subpasta.exists():
            destino = subpasta / arquivo.name
            if destino.exists():
                print("Arquivo já existe")
            else:
                shutil.move(arquivo, destino)
            data_formatada = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            with open('logs.txt', 'a', encoding='utf-8') as log:
                log.write(f'{data_formatada} | {arquivo} movido para {subpasta} \n')
            if nome_categoria in contagem_de_movimentos:
                contagem_de_movimentos[nome_categoria] +=1
            else:
                contagem_de_movimentos[nome_categoria] = 1    
            print(f'Arquivo {arquivo.name} movido para {nome_categoria}')
        else:
            print(f'ERROR: Conflito o arquivo {arquivo} ja existe na pasta {nome_categoria}')
    for categoria, total in contagem_de_movimentos.items():
        print(f'Foram movidos {total} arquivos para a pasta {categoria}')            

descompactar_arquivo('organizador.zip', 'arquivos')
organizar_arquivo('arquivos')
print('Concluido com sucesso')



        
    


    
