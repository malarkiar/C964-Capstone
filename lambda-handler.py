import json

def get_results(asset, amount):
    q_asset = get_most_correlated_asset(asset)
    b_predict = predict_price(asset)
    q_predict = predict_price(q_asset)
    p_delta = get_prediction_delta(b_predict, q_predict)


    return [{
        "bAsset": asset,
        "qAsset": q_asset['symbol'],
        "bqCorrelation": q_asset['correlation'],
        "amount": amount,
        "bPredictMin": b_predict['min'],
        "bPredictMax": b_predict['max'],
        "qPredictMin": q_predict['min'],
        "qPredictMax": q_predict['max'],
        "predictDeltaMin": p_delta['min'],
        "predictDeltaMax": p_delta['max']
    }]


def get_most_correlated_asset(asset):
    return {
        "symbol": "ETH",
        "correlation": 0.88
    }


def predict_price(asset):
    price_prediction = 1000
    uncertainty = 0.04

    return {'prediction': price_prediction, 'uncertainty': uncertainty}


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
