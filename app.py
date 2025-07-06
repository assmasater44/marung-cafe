from flask import Flask, render_template, url_for
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/location')
def location():
    return render_template('location.html')

if __name__ == '__main__':
    print("Serving on port 5050...")
    serve(app, host="0.0.0.0", port=5050)
