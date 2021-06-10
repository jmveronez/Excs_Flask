from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask rodando :D</h1>"

@app.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Olá "+nome+"<br />Seja bem Vindo!</h1></center>"

@app.route("/auladeontem/")
def carrega():
    return render_template('index.html')

if (__name__ == "__main__"):
    app.run(debug=True)