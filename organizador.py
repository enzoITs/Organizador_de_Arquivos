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
        diretorio_organizado.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(zip_desorganizado, diretorio_organizado)
    except Exception as erro:
        print(f'Arquivo corrompido {erro}')

# registro de log
def registro_log(mensagem):
    data_formatada = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('logs.txt', 'a', encoding='utf-8') as log:
        log.write(f'{data_formatada} | {mensagem} \n')


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

def main():
    descompactar_arquivo('organizador.zip', 'arquivos')
    organizar_arquivo('arquivos')
    print('Concluido com sucesso')

if __name__ == "__main__":
    main()



        
    


    
