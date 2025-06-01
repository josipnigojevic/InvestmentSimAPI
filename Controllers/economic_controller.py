from Services.economic_service import get_economic_indicator_data

def get_economic_indicator_information(series_id):
    economic_data = get_economic_indicator_data(series_id)
    if economic_data:
        return economic_data, 200
    return {"error": "Economic indicator data not found."}, 404