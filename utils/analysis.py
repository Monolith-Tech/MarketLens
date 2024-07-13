# analysis.py
# Script for analyzing data using large language models (LLMs).

import openai

# Your OpenAI API key
openai.api_key = 'your-openai-api-key'

def extract_keywords(text):
    """
    Extracts key phrases from the given text using an LLM.

    :param text: str, the text from which to extract key phrases
    :return: str, extracted key phrases
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Extract key phrases from the following text: {}".format(text),
        max_tokens=60
    )
    return response.choices[0].text.strip()

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text using an LLM.

    :param text: str, the text to analyze for sentiment
    :return: str, the sentiment classification (Positive, Neutral, Negative)
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Analyze the sentiment of the following text: {}".format(text),
        max_tokens=10
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    text_example = "The new market trend is shifting rapidly due to recent tech advancements."
    keywords = extract_keywords(text_example)
    sentiment = analyze_sentiment(text_example)
    print("Keywords:", keywords)
    print("Sentiment:", sentiment)
