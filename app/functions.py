def getCorrelatedAssets(symbol):
    if symbol == 'BTC':
        ethObj = {
            "label": "ETH",
            "correlation_score": .920,
            "graph_image": "eth_btc.jpeg",
            "graph_width": 600,
            "graph_height": 200,
            "graph_alt": "ETH/BTC Correlation"
        }

        ltcObj = {
            "label": "LTC",
            "correlation_score": .871,
            "graph_image": "ltc_btc.jpeg",
            "graph_width": 600,
            "graph_height": 200,
            "graph_alt": "LTC/BTC Correlation"
        }

        avaxObj = {
            "label": "AVAX",
            "correlation_score": .774,
            "graph_image": "avax_btc.jpeg",
            "graph_width": 600,
            "graph_height": 200,
            "graph_alt": "AVAX/BTC Correlation"
        }
        return [ethObj, ltcObj, avaxObj]


def getPricePrediction(symbol, period):
    if symbol == 'ETH':
        ethObj = {
            "label": "ETH",
            "weeks_future": period,
            "future_price": 4165,
            "graph_image": "eth_btc.jpeg",
            "graph_width": 600,
            "graph_height": 200,
            "graph_alt": "ETH Future Price"
        }

        return ethObj
