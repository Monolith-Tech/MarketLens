# st_app.py
# Streamlit interface for displaying analysis results.

import streamlit as st
import web
import analysis

st.title('Market Trend Analyzer')

# User inputs
url = st.text_input('Enter URL to scrape for news:')
keyword = st.text_input('Enter keyword for Twitter search:')

if st.button('Analyze Trends'):
    # Fetching data
    news_articles = web.scrape_news(url)
    tweets = web.fetch_tweets(keyword, count=20)

    # Analyzing data
    articles_keywords = [analysis.extract_keywords(article) for article in news_articles]
    tweets_sentiments = [analysis.analyze_sentiment(tweet) for tweet in tweets]

    # Displaying results
    st.write("### News Articles Keywords:")
    st.write(articles_keywords)

    st.write("### Tweets Sentiments:")
    st.write(tweets_sentiments)

# Run this script by using: streamlit run st_app.py
