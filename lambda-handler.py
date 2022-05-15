import json

def get_results(asset, amount):
    q_asset = get_most_correlated_asset(asset)
    b_predict = predict_price(asset)
    q_predict = predict_price(q_asset)
    p_delta = get_prediction_delta(b_predict, q_predict)

    return [{
        "bAsset": asset,
        "qAsset": q_asset.get("symbol"),
        "bqCorrelation": q_asset.get("correlation"),
        "amount": amount,
        "bPredict": b_predict,
        "qPredict": q_predict,
        "predictDelta": p_delta
    }]


def get_most_correlated_asset(asset):
    return {
        "symbol": "ETH",
        "correlation": 0.88
    }


def predict_price(asset):
    price_prediction = 1000
    return price_prediction


def get_prediction_delta(b_predict, q_predict):
    return (q_predict/b_predict - 1) * 100


def handle(event, context):
    asset = json.loads(event.get('body')).get('asset')
    amount = json.loads(event.get('body')).get('amount')
    response = get_results(asset, amount)
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
