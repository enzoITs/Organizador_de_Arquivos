# -*- coding: utf-8 -*-

import shutil
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, Optional

mapa_extensao = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Executaveis": [".exe", ".msi", ".sh"],
}


def registro_log(mensagem: str, *, log_path: str = "logs.txt") -> None:
    data_formatada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"{data_formatada} | {mensagem}\n")


def organizar_pasta(
    pasta_para_organizar: Path,
    *,
    on_message: Optional[Callable[[str], None]] = None,
    log_path: str = "logs.txt",
) -> Dict[str, int]:
    contagem_de_movimentos: Dict[str, int] = {}

    def emitir(mensagem: str) -> None:
        if on_message is not None:
            on_message(mensagem)
        else:
            print(mensagem)

    if not pasta_para_organizar.exists() or not pasta_para_organizar.is_dir():
        raise FileNotFoundError("Pasta não existe (ou não é um diretório).")

    for arquivo in pasta_para_organizar.iterdir():
        if not arquivo.is_file():
            continue

        nome_categoria = "Outros"
        for categoria, extensoes in mapa_extensao.items():
            if arquivo.suffix.lower() in extensoes:
                nome_categoria = categoria
                break

        subpasta = pasta_para_organizar / nome_categoria
        subpasta.mkdir(exist_ok=True, parents=True)
        destino = subpasta / arquivo.name

        if destino.exists():
            emitir(f"Arquivo já existe: {destino.name}")
            continue

        try:
            shutil.move(str(arquivo), str(destino))
        except Exception as exc:
            emitir(f"Falha ao mover {arquivo.name}: {exc}")
            continue

        registro_log(f"{arquivo} movido para {destino}", log_path=log_path)
        contagem_de_movimentos[nome_categoria] = contagem_de_movimentos.get(nome_categoria, 0) + 1
        emitir(f"Arquivo {arquivo.name} movido para {nome_categoria}")

    for categoria, total in contagem_de_movimentos.items():
        emitir(f"Foram movidos {total} arquivos para a pasta {categoria}")

    return contagem_de_movimentos


def organizar_arquivo_interativo() -> Dict[str, int]:
    local = input("Digite o caminho da pasta: ").strip().strip('"')
    if not local:
        raise ValueError("Caminho vazio.")
    return organizar_pasta(Path(local))


def main() -> None:
    organizar_arquivo_interativo()
    print("Concluído com sucesso")


if __name__ == "__main__":
    main()

