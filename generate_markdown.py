import json

# Carregar o arquivo JSON
with open("products.json") as f:
    data = json.load(f)

# Ordenar os dados por 'category' e 'product_name'
data.sort(key=lambda x: (x['category'], x['product_name']))


# Agrupar os dados por categoria
grouped_data = {}
for item in data:
    category = item["category"]
    if category not in grouped_data:
        grouped_data[category] = []
    grouped_data[category].append(item)

# Criar o markdown
markdown = " # Azure Products \n"


for category, items in grouped_data.items():
    markdown += f"## {category}\n"
    markdown += "| Image | Product Name |\n"
    markdown += "|---|---|\n"
    for item in items:
        markdown += f'| <img src="./{item["folder"]}" width="30"> | {item["product_name"]} |\n'
    markdown += "\n\n"
    markdown += "---\n"
    # Salvar o markdown em um arquivo
with open("README.md", "w") as f:
    f.write(markdown)
