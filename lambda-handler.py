import json


def get_correlations(asset):
    # TODO
    return True


def get_predictions(asset, amount):
    # TODO
    return True


def get_result(asset, amount):
    correlation_response = get_correlations(asset)
    prediction_response = get_predictions(asset, amount)
    return True


def handle(event, context):
    response = {}
    asset = json.loads(event.get('body')).get('asset')
    amount = json.loads(event.get('body')).get('amount')
    response = get_result(asset, amount)
    return {
        "statusCode": 200,
        "body": json.dumps(response)
        # "body": json.dumps([{
        #     "bAsset": "BTC",
        #     "qAsset": "ETH",
        #     "bqCorrelation": "0.55",
        #     "amount": "100",
        #     "bPredict": "98",
        #     "qPredict": "88",
        #     "predictDelta": "10%"
        # }])
    }
