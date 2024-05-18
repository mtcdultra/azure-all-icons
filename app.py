from flask import Flask, render_template
import json
from collections import defaultdict

app = Flask(__name__)

@app.route('/')
def index():
    # Carregar o arquivo JSON
    with open('products.json') as f:
        data = json.load(f)
    
    # Organizar os produtos por categoria
    products_by_category = defaultdict(list)
    for product in data:
        products_by_category[product['category']].append(product)
    
    # Passar os dados para o template
    return render_template('index.html', products_by_category=products_by_category)

if __name__ == '__main__':
    app.run(debug=True)
