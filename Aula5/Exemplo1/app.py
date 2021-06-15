from typing import Coroutine
from flask import Flask, app, render_template, request

app = Flask(__name__)

@app.route("/", methods=('GET','POST'))
def index():
    nome=None
    sobrenome=None
    criatura=None
    imagem=None

    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        criatura = request.form['criatura']

        if criatura.upper() == "ELFO":
            imagem = "static/download.jpg"
        elif criatura.upper() == "JAVALI":
            imagem = "static/Big_Boar_Rampage.png"
        elif criatura.upper() == "DEMONIO":
            imagem = "static/demonho.jpg"
        
    return render_template("index.html", nome=nome,sobrenome=sobrenome,criatura=criatura,imagem=imagem)

if (__name__ == "__main__"):
    app.run(debug=True)