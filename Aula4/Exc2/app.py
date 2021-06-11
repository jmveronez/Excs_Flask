from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nome = "João Marco"
    idade = 20
    if idade >= 18:
        maioridade = True
    else:
        maioridade = False
    cidade = "Ribeirão Preto"
    imagem = "/static/blue.jpg"
    return render_template('index.html',nome=nome,idade=idade,cidade=cidade,imagem=imagem,maioridade=maioridade)

if (__name__ == "__main__"):
    app.run(debug=True)