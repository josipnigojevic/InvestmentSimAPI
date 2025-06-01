from Services.analytics_service import get_technical_indicators

def get_stock_technical_analysis(symbol, period="1y"):
    analysis_data = get_technical_indicators(symbol, period)
    if analysis_data:
        historical_data = {date: data for date, data in analysis_data.items() if data['Predicted_Close'] is None}
        future_predictions = {date: data['Predicted_Close'] for date, data in analysis_data.items() if data['Predicted_Close'] is not None}
        
        return {
            "historical_data": historical_data,
            "future_predictions": future_predictions
        }, 200
    return {"error": "Technical analysis data not found."}, 404