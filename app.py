from flask import Flask
from flask_migrate import Migrate
from Models.user_model import db as user_db, User
from Models.portfolio_model import Portfolio
from Routes.stock_routes import stock_routes
from Routes.portfolio_routes import portfolio_routes
from Routes.user_routes import user_routes
from Routes.company_routes import company_routes
from Routes.market_routes import market_routes
from Routes.economic_routes import economic_routes
from Routes.analytics_routes import analytics_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/investment_simulator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(stock_routes, url_prefix='/api/v1/stocks')
app.register_blueprint(portfolio_routes, url_prefix='/api/v1/portfolio')
app.register_blueprint(user_routes, url_prefix='/api/v1/users')
app.register_blueprint(company_routes, url_prefix='/api/v1/company')
app.register_blueprint(market_routes, url_prefix='/api/v1/market')
app.register_blueprint(economic_routes, url_prefix='/api/v1/economic')
app.register_blueprint(analytics_routes, url_prefix='/api/v1/analytic')

user_db.init_app(app)
migrate = Migrate(app, user_db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
