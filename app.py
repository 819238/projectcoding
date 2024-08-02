from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pages():
    # Contoh data produk
    products = [
        {'id': 1, 'name': 'Produk 1', 'price': 100000},
        {'id': 2, 'name': 'Produk 2', 'price': 150000},
        {'id': 3, 'name': 'Produk 3', 'price': 200000},
    ]
    return render_template('page.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
