# controllers/portfolio_controller.py
from Services.portfolio_service import *

def create_user_portfolio(user_id):
    portfolio = create_portfolio(user_id)
    if portfolio:
        return {"message": "Portfolio created successfully.", "portfolio": portfolio.to_dict()}, 200
    return {"message": "Failed to create portfolio."}, 400

def buy_stock(user_id, symbol, shares):
    success = buy_stock_in_portfolio(user_id, symbol, shares)
    if success:
        return {"message": "Stock purchased successfully."}, 200
    return {"message": "Insufficient balance to buy the stock."}, 400

def sell_stock(user_id, symbol, shares):
    success = sell_stock_in_portfolio(user_id, symbol, shares)
    if success:
        return {"message": "Stock sold successfully."}, 200
    return {"message": "Insufficient shares to sell."}, 400

def get_portfolio(user_id):
    portfolio_data = get_user_portfolio(user_id)
    if portfolio_data:
        return portfolio_data, 200
    return {"message": "Portfolio not found."}, 404

def get_portfolio_total_value(user_id):
    portfolio_value = get_portfolio_value(user_id)
    if portfolio_value:
        return portfolio_value, 200
    return {"message": "Portfolio not found or empty."}, 404
