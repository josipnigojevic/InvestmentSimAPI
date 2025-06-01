import requests
import logging
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

NEWS_API_KEY = '105b8d461571427f9d58e9f39650e19e'

logging.basicConfig(level=logging.DEBUG)

def fetch_financial_news(symbol):
    api_url = f'https://newsapi.org/v2/everything?q={symbol}&apiKey={NEWS_API_KEY}'
    logging.debug(f"Requesting financial news from {api_url}")
    response = requests.get(api_url)
    
    if response.status_code == 200:
        news_data = response.json()
        logging.debug(f"Financial news data: {news_data}")
        articles = news_data.get('articles', [])
        return articles
    else:
        logging.error(f"Failed to fetch financial news: {response.status_code}")
        return []

def analyze_sentiment(articles):
    sid = SentimentIntensityAnalyzer()
    for article in articles:
        description = article.get('description')
        if description:
            sentiment_score = sid.polarity_scores(description)
            article['sentiment'] = sentiment_score
        else:
            article['sentiment'] = {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
    return articles

def get_financial_news_with_sentiment(symbol):
    articles = fetch_financial_news(symbol)
    if articles:
        articles_with_sentiment = analyze_sentiment(articles)
        return articles_with_sentiment
    return []