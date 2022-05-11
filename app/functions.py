def getCorrelatedAssets():
    return {
        "btc": {
            "eth": {
                    "rAsset": "ETH",
                    "cRatio": 0.44,
                    "eReturn%": None,
                    "eReturn": None,
                    "eReturn%Delta": None,
                    "eReturnDelta": None
            }
        }
    }


def appendPredictions(asset_list, r_amount):
    asset_list['btc'][0]['eReturn%'] = '+7%'
    asset_list['btc'][0]['eReturn'] = '+201'
    asset_list['btc'][0]['eReturn%Delta'] = '-1%'
    asset_list['btc'][0]['eReturnDelta'] = '-28'
    return asset_list
