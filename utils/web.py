# web.py
# Script for web scraping and data fetching from APIs.

import requests
from bs4 import BeautifulSoup
import tweepy  # Twitter API

# Configuration for Twitter API (replace with your own keys)
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Setting up Twitter API access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def scrape_news(url):
    """
    Scrapes news articles from a given URL.

    :param url: str, the URL of the news website to scrape
    :return: list of str, extracted articles text
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    return [article.text.strip() for article in articles]

def fetch_tweets(keyword, count=10):
    """
    Fetches tweets containing a specific keyword using the Twitter API.

    :param keyword: str, the keyword to search for in tweets
    :param count: int, the number of tweets to fetch
    :return: list of str, the text of the fetched tweets
    """
    tweets = api.search(q=keyword, count=count)
    return [tweet.text for tweet in tweets]

# Example usage
if __name__ == "__main__":
    news_articles = scrape_news("https://example-news-site.com")
    tweets = fetch_tweets("market trend", count=20)
