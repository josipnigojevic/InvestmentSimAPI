from Services.market_service import get_market_index_data

def get_market_index_information(symbol):
    market_data = get_market_index_data(symbol)
    if market_data:
        return market_data, 200
    return {"error": "Market index data not found."}, 404