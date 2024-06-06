import os
import json


def listar_arquivos(diretorio):
    # Primeiro, renomeie os diretórios
    for root, dirs, _ in os.walk(
        diretorio, topdown=False
    ):  # topdown=False para que possamos renomear os subdiretórios primeiro
        for dir in dirs:
            new_dir = dir.replace(" ", "")
            os.rename(os.path.join(root, dir), os.path.join(root, new_dir))

    # Lista para armazenar os caminhos dos arquivos e suas categorias
    caminhos_dos_arquivos = []

    # Agora, processe os arquivos
    for root, _, files in os.walk(diretorio):
        for file in files:
            # Exclui o arquivo .DS_Store se encontrado
            if file == ".DS_Store":
                os.remove(os.path.join(root, file))
                continue

            # Remove espaços em branco no nome do arquivo
            new_file = file.replace(" ", "")
            os.rename(os.path.join(root, file), os.path.join(root, new_file))

            # Constrói o caminho completo para o arquivo
            caminho_completo = os.path.join(root, new_file)

            # Obtém a categoria (nome da subpasta imediatamente após 'Icons')
            relative_path = os.path.relpath(caminho_completo, diretorio)
            parts = relative_path.split(os.sep)
            category = parts[0].capitalize() if len(parts) > 1 else ""

            # Adiciona o caminho, categoria e nome do arquivo à lista
            caminhos_dos_arquivos.append(
                {
                    "folder": os.path.join("/", diretorio, relative_path).replace(
                        "\\", "/"
                    ),  # Corrige o caminho para ser acessível a partir do HTML
                    "category": category,
                    "product_name": (
                        new_file.split("-icon-service-")[1]
                        .replace(".svg", "")
                        .replace("-", " ")
                        if "-icon-service-" in new_file
                        else ""
                    ),
                }
            )

    return caminhos_dos_arquivos


# Define o diretório inicial
diretorio_inicial = "static/Icons"

# Chama a função para listar arquivos
caminhos_dos_arquivos = listar_arquivos(diretorio_inicial)

# Salva a lista de caminhos dos arquivos em um arquivo JSON
with open("products.json", "w") as json_file:
    json.dump(caminhos_dos_arquivos, json_file, indent=4)

print("Caminhos dos arquivos salvos em 'caminhos_dos_arquivos.json'")
