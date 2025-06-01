
# API Documentation

This API empowers users and developers to access robust financial data, analytics, news insights, portfolio management capabilities, and economic indicators seamlessly while also giving investment advice depending on the compound sentiment of the latest news related to each company.

## Features

### User Management
- **Create User**: Sign up new users with email and username.
- **Delete User**: Remove users by user ID.
- **Retrieve User Data**: Access detailed user information.
- **List Users**: Fetch a list of all users.

### Financial Analytics
- **Technical Indicators**: Provides advanced analytics including SMA, RSI, MACD, and Bollinger Bands.
- **Price Predictions**: Implements linear regression models to forecast future stock prices.

### Company Data
- **Detailed Company Information**: Acquire comprehensive data from Yahoo Finance on companies.

### Economic Data
- **Economic Indicators**: Retrieve critical economic metrics sourced from the FRED API.

### Market Information
- **Market Index Data**: Obtain real-time and historical market index information.

### Financial News and Sentiment
- **News Articles**: Access relevant financial news articles via NewsAPI.
- **Sentiment Analysis**: Apply sentiment analysis to news articles to gauge market sentiment using NLTK's VADER.

### Portfolio Management
- **Create and Manage Portfolios**: Set up user portfolios for managing investments.
- **Stock Transactions**: Enable buying and selling of stocks within portfolios.
- **Real-Time Portfolio Valuation**: Instantly value portfolios based on current stock market prices.

### Stock Information
- **Real-Time Stock Prices**: Fetch the latest prices for stocks using Alpha Vantage.
- **Historical Stock Data**: Access detailed historical pricing data, customizable by date ranges and intervals.

## Dependencies
- Python libraries: yfinance, pandas-ta, sklearn, requests, nltk
- APIs: Alpha Vantage, FRED, NewsAPI

## Getting Started
Ensure you have your API keys configured for the external data providers listed above. Clone the repository, install the dependencies, and run the API locally or deploy it to your chosen hosting service or use the dockerfile i provided.

```

git clone \[repository-url]
cd \[repository-name]
pip install -r requirements.txt

```

## Support
For support, issues, or feature requests, please contact the me through GitHub Issues. Stay tuned for more updates!

Josip Nigojević

