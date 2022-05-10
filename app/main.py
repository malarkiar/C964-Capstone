from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/sub", methods=["POST"])
def submit():
    # HTML -> .py
    if request.method == "POST":
        name = request.form["username"]
    # .py -> HTML
    return render_template("submit.html", n = name)

