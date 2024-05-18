import os
import json

def listar_arquivos(diretorio):
    # Lista para armazenar os caminhos dos arquivos e suas categorias
    caminhos_dos_arquivos = []

    # Percorre todos os diretórios e arquivos na árvore de diretórios a partir do diretório raiz
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            # Exclui o arquivo .DS_Store se encontrado
            if file == '.DS_Store':
                os.remove(os.path.join(root, file))
                continue

            # Constrói o caminho completo para o arquivo
            caminho_completo = os.path.join(root, file)
            
            # Obtém a categoria (nome da subpasta imediatamente após 'Icons')
            relative_path = os.path.relpath(caminho_completo, diretorio)
            parts = relative_path.split(os.sep)
            category = parts[0].capitalize() if len(parts) > 1 else ""

            # Extrai o product_name a partir do nome do arquivo
            product_name = ""
            if "-icon-service-" in file:
                product_name = file.split("-icon-service-")[1].replace(".svg", "").replace("-", " ")
            
            # Adiciona o caminho, categoria e product_name à lista
            caminhos_dos_arquivos.append({
                "folder": caminho_completo,
                "category": category,
                "product_name": product_name
            })

    return caminhos_dos_arquivos

# Define o diretório inicial
diretorio_inicial = 'Icons'

# Chama a função para listar arquivos
caminhos_dos_arquivos = listar_arquivos(diretorio_inicial)

# Salva a lista de caminhos dos arquivos em um arquivo JSON
with open('products.json', 'w') as json_file:
    json.dump(caminhos_dos_arquivos, json_file, indent=4)

print("Caminhos dos arquivos salvos em 'caminhos_dos_arquivos.json'")
