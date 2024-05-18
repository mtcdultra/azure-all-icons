from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('products.json') as f:
        data = json.load(f)

    return render_template('index.html', products=data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)