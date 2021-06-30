from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Configurações de acesso ao banco de dados

user = 'rcdryyxc'
password = 'AfKxshxwEsI72VPIR0y7OZ5UvvQWJ2bO'
host = 'tuffi.db.elephantsql.com'
database = 'rcdryyxc'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Uma chave secreta bem secreta"

db = SQLAlchemy(app)

# Modelar a classe Filmes ->  Table Filmes
class filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
    
    @staticmethod
    def read_all():
        return filme.query.order_by(filme.id.asc()).all()

    @staticmethod
    def read_index():
        filmes = []
        filmes1 = filmes.append(filme.query.order_by(filme.id.asc()).limit(3).all())
        filmes2 = filmes.append(filme.query.order_by(filme.id.desc()).limit(3).all())
        filmes3 = filmes.append(filme.query.order_by(filme.nome.asc()).limit(3).all())
        filmes4 = filmes.append(filme.query.order_by(filme.nome.desc()).limit(3).all())
        filmes_aleatorios = random.choice(filmes)
        return filmes_aleatorios


@app.route("/")
def index():
    registros = filme.read_index()
    return render_template("index.html", registros=registros)

@app.route("/read")
def read_all():
    # Chamada do método Read_all da classe Filmes, que representa a tabela de filmes do banco de dados.
    registros = filme.read_all()
    print(registros)
    return render_template("read_all.html", registros=registros)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/read/<id_registro>")
def read_id(id_registro):
    registro = filme.read_id(id_registro)

if (__name__ == '__main__'):
    app.run(debug=True)