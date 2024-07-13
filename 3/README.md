# Project Overview

## Title
Market Trend Analyzer

## Objective
The Market Trend Analyzer is designed to capture, analyze, and visualize market trends in real time using advanced technologies such as web scraping, natural language processing, and machine learning. It aims to provide actionable insights into market dynamics through an interactive application powered by Streamlit, enhanced with a responsive chatbot for user queries regarding market trends.

## Technical Components

### 1. Data Collection (`web.py`)
- **Purpose**: Fetch real-time data from various online sources like news websites and social media platforms, focusing on market-related content.
- **Technologies Used**: Python, `requests`, `BeautifulSoup` for HTML scraping, and `tweepy` for accessing the Twitter API.
- **Functionality**:
  - `scrape_news`: Scrapes news articles using `BeautifulSoup` to parse HTML and extract textual content.
  - `fetch_tweets`: Gathers tweets related to specific market trends via the Twitter API.

### 2. Data Analysis (`analysis.py`)
- **Purpose**: Analyze collected data by extracting keywords, assessing sentiment, and aggregating information to identify key market trends.
- **Technologies Used**: Python, OpenAI GPT for text extraction and analysis.
- **Functionality**:
  - `extract_keywords`: Extracts key phrases from texts using OpenAI's GPT models.
  - `analyze_sentiment`: Determines the sentiment (positive, neutral, negative) of texts.
  - `aggregate_data`: Aggregates keywords and sentiments into a structured format for further analysis and visualization.

### 3. User Interface (`st_app.py`)
- **Purpose**: Provide a user-friendly interface for real-time interaction with the Market Trend Analyzer, displaying data and integrating a chatbot.
- **Technologies Used**: Streamlit.
- **Functionality**:
  - Interactive forms for user inputs, defining parameters for data collection.
  - Data visualization using graphs and charts.
  - Chatbot integration for dynamic user interaction regarding market insights.

### 4. Chatbot Module (`chatbot.py`)
- **Purpose**: Answer user queries about market trends using a context-aware, retrieval-augmented approach.
- **Technologies Used**: Python, OpenAI API.
- **Functionality**:
  - `generate_response`: Uses OpenAI's GPT models to respond to user queries based on aggregated data and contextual knowledge.

## System Architecture
- **Front-End**: Streamlit-based interface for user interactions and visualizations.
- **Back-End**: Python scripts for data scraping, processing, and analysis.
- **Data Flow**:
  - User inputs trigger data collection via `web.py`.
  - Collected data is processed by `analysis.py` to extract insights.
  - Insights are visualized and made interactively available via the Streamlit interface.
  - The chatbot in `chatbot.py` uses processed data to dynamically respond to user queries.

## Deployment and Operation
- **Deployment Environment**: Capable of running on local servers or cloud platforms that support Python and Streamlit.
- **Execution**: Users launch the application via Streamlit, initiating the interactive web interface.

## Conclusion
The Market Trend Analyzer is a robust and sophisticated tool for in-depth market analysis. Its modular design allows for independent updates and scalability, ensuring it remains a valuable asset for market analysts, businesses, investors, and policymakers.
