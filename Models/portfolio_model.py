from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from Models import db

class Investment(db.Model):
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), nullable=False)
    shares = Column(Float, nullable=False)
    purchase_price = Column(Float, nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'), nullable=False)

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'shares': self.shares,
            'purchase_price': self.purchase_price
        }

class Portfolio(db.Model):
    id = Column(Integer, primary_key=True)
    cash_balance = Column(Float, nullable=False, default=100000.0)
    investments = relationship('Investment', backref='portfolio', lazy=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def buy_stock(self, symbol, shares, price_per_share):
        total_cost = shares * price_per_share
        if self.cash_balance >= total_cost:
            self.cash_balance -= total_cost
            investment = next((inv for inv in self.investments if inv.symbol == symbol), None)
            if investment:
                investment.shares += shares
                investment.purchase_price = price_per_share  
            else:
                new_investment = Investment(symbol=symbol, shares=shares, purchase_price=price_per_share, portfolio_id=self.id)
                db.session.add(new_investment)
            db.session.commit()
            return True
        return False

    def sell_stock(self, symbol, shares, price_per_share):
        investment = next((inv for inv in self.investments if inv.symbol == symbol), None)
        if investment and investment.shares >= shares:
            total_revenue = shares * price_per_share
            self.cash_balance += total_revenue
            investment.shares -= shares
            if investment.shares == 0:
                db.session.delete(investment)
            db.session.commit()
            return True
        return False

    def calculate_total_value(self, get_current_stock_price):
        total_investments_value = sum(
            inv.shares * get_current_stock_price(inv.symbol) for inv in self.investments
        )
        return self.cash_balance + total_investments_value

    def to_dict(self):
        return {
            'cash_balance': self.cash_balance,
            'investments': [inv.to_dict() for inv in self.investments]
        }