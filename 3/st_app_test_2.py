# st_app.py
# Streamlit interface for displaying analysis results and interacting with a chatbot.

import streamlit as st
import web
import analysis
from chatbot import generate_response

st.title('Market Trend Analyzer')

# Sections for data input and analysis
url = st.text_input('Enter URL to scrape for news:')
keyword = st.text_input('Enter keyword for Twitter search:')
if st.button('Analyze Trends'):
    news_articles = web.scrape_news(url)
    tweets = web.fetch_tweets(keyword, count=20)
    articles_keywords = [analysis.extract_keywords(article) for article in news_articles]
    tweets_sentiments = [analysis.analyze_sentiment(tweet) for tweet in tweets]
    aggregated_data = analysis.aggregate_data(articles_keywords, tweets_sentiments)
    st.write("### News Articles Keywords and Sentiments:")
    st.json(aggregated_data)

# Chatbot section
st.write("## Market Trend Chatbot")
user_query = st.text_input("Ask me anything about recent market trends:")
if user_query:
    # Convert aggregated data to a readable format for the chatbot
    readable_context = ', '.join([f"{key} mentioned {value['count']} times with sentiments {value['positive']} positive, {value['neutral']} neutral, {value['negative']} negative" for key, value in aggregated_data.items()])
    chat_response = generate_response(user_query, readable_context)
    st.write("### Response:")
    st.write(chat_response)

# Example command to run this Streamlit app: streamlit run st_app.py
