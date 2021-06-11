from flask import Blueprint, render_template

bp = Blueprint('bp',__name__)

@bp.route("/")
def home():
    return "<h1>Flask rodando :D</h1>"

@bp.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Olá "+nome+"<br />Seja bem Vindo!</h1></center>"

@bp.route("/auladeontem/")
def carrega():
    return render_template('index.html')