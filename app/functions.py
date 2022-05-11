def get_results(asset, value):
    q_asset = get_most_correlated_asset(asset)
    b_predict = predict_price(asset)
    q_predict = predict_price(q_asset)
    p_delta = get_prediction_delta(b_predict, q_predict)

    return [{
        "bAsset": asset,
        "qAsset": q_asset['symbol'],
        "bqCorrelation": q_asset['correlation'],
        "amount": value,
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
