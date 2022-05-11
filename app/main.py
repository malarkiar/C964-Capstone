from flask import Flask, render_template, request
from app.functions import getCorrelatedAssets, appendPredictions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    asset_list = getCorrelatedAssets()
    if request.method == 'POST':
        r_amount = request.form["r_amount"]
        asset_list = appendPredictions(asset_list, r_amount)
    return render_template("index.html", list=asset_list)



