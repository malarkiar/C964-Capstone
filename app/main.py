from flask import Flask, render_template, request
from app.functions import getCorrelatedAssets, getPricePrediction

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/correlated-assets/", methods=["POST"])
def correlatedAssets():
    # HTML -> .py
    if request.method == 'POST':
        crypto = request.form["crypto"]
    # .py -> HTML
    correlated_assets = getCorrelatedAssets(crypto)
    return render_template("correlated-assets.html", c=crypto, list=correlated_assets)


@app.route("/price-prediction/", methods=["POST"])
def pricePrediction():
    # HTML -> .py
    if request.method == 'POST':
        crypto = request.form["crypto"]
        period = request.form["period"]
    # .py -> HTML
    price_prediction = getPricePrediction(crypto, period)
    return render_template("price-prediction.html", c=crypto, t=period, p=price_prediction)

