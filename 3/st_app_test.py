# st_app.py
# Streamlit interface for displaying analysis results.

import streamlit as st
import web
import analysis

st.title('Market Trend Analyzer')

# User inputs
url = st.text_input('Enter URL to scrape for news:')

if st.button('Analyze Trends'):
    # Fetching data
    news_articles = web.scrape_news(url)

    # Analyzing data
    keywords = [analysis.extract_keywords(article) for article in news_articles]
    sentiments = [analysis.analyze_sentiment(article) for article in news_articles]
    aggregated_data = analysis.aggregate_data(keywords, sentiments)

    # Displaying results
    st.write("### Keywords:")
    st.write(keywords)

    st.write("### Sentiments:")
    st.write(sentiments)
    
    st.write("### Aggregated_data")
    st.write(aggregated_data)


