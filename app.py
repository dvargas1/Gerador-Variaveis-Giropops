import random
from flask import Flask, render_template

app = Flask(__name__)

# Lista de frases
frases = [
    "giropops",
    "giropops-strigus-girus",
    "strigus",
    "strigus-girus",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frase')
def obter_frase():
    frase_aleatoria = random.choice(frases)
    return frase_aleatoria

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
