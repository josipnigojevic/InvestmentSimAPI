from Models.portfolio_model import Portfolio, db
from Models.user_model import User
from Services.stock_service import get_real_time_stock_price

def create_portfolio(user_id):
    user = User.query.get(user_id)
    if user and not user.portfolio:
        portfolio = Portfolio(user_id=user_id)
        db.session.add(portfolio)
        db.session.commit()
        return portfolio
    return None

def get_user_portfolio(user_id):
    user = User.query.get(user_id)
    if user and user.portfolio:
        return user.portfolio.to_dict()
    return None

def buy_stock_in_portfolio(user_id, symbol, shares):
    user = User.query.get(user_id)
    if user and user.portfolio:
        current_price = get_real_time_stock_price(symbol)['price']
        success = user.portfolio.buy_stock(symbol, shares, float(current_price))
        return success
    return False

def sell_stock_in_portfolio(user_id, symbol, shares):
    user = User.query.get(user_id)
    if user and user.portfolio:
        current_price = get_real_time_stock_price(symbol)['price']
        success = user.portfolio.sell_stock(symbol, shares, float(current_price))
        return success
    return False

def get_portfolio_value(user_id):
    user = User.query.get(user_id)
    if user and user.portfolio:
        total_value = user.portfolio.calculate_total_value(
            lambda symbol: float(get_real_time_stock_price(symbol)['price'])
        )
        portfolio_value = user.portfolio.to_dict()
        portfolio_value['total_value'] = total_value
        return portfolio_value
    return None