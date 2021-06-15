from re import DEBUG
from flask import Flask, app, render_template, request
import flask

app = flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if (__name__ == "__main__"):
    app.run(debug=True)