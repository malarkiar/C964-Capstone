from flask import Flask, render_template, request
from app.functions import getCorrelatedAssets

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/results/", methods=["POST"])
def returnResults():
    asset = request.form["asset"]
    value = request.form["value"]
    return render_template("return-results.html", a=asset, v=value)
