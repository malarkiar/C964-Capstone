from flask import Flask, render_template, request
from app.functions import get_results

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/results/", methods=["POST"])
def return_results():
    asset = request.form["asset"]
    value = request.form["value"]
    predictions = get_results(asset, value)
    return render_template("return-results.html", p=predictions)
