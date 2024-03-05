from flask import Flask, render_template

app = Flask(__name__, static_url_path='/images')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)