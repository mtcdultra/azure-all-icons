import os
import json
from flask import Flask, render_template

app = Flask(__name__)

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

            # Adiciona o caminho, categoria e nome do arquivo à lista
            caminhos_dos_arquivos.append({
                "folder": os.path.join("/", diretorio, relative_path).replace("\\", "/"),  # Corrige o caminho para ser acessível a partir do HTML
                "category": category,
                "product_name": file.split("-icon-service-")[1].replace(".svg", "").replace("-", " ") if "-icon-service-" in file else ""
            })

    return caminhos_dos_arquivos

# Define a rota para renderizar o template HTML
@app.route('/')
def index():
    # Define o diretório inicial
    diretorio_inicial = 'Icons'
    
    # Chama a função para listar arquivos
    produtos = listar_arquivos(diretorio_inicial)

    # Renderiza o template HTML com a lista de produtos
    return render_template('index.html', products=produtos)

if __name__ == "__main__":
    # Executa a aplicação Flask
    app.run(debug=True, port=5001)
