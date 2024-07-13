import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI, OpenAIError
from typing import Dict, List


# OpenAI client
class OpenAIClient:
    def __init__(self, model: str = "gpt-4-1106-preview", system_prompt: str = "You are a helpful assistant that can answer questions and help with tasks.") -> None:
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'],)
        self.model = model.strip()
        self.temperature = 0.3
        self.system_prompt = system_prompt

    def generate_response(self, prompt: Dict[str, str]) -> str:
        response = self.client.chat.completions.create(
            model = self.model,
            messages = prompt,
            temperature = self.temperature
        )
        output = response.choices[0].message.content
        return output
    
    def get_output(self, prompt: str) -> str:
        prompt = [
            {'role': 'system', 'content': self.system_prompt},
            {'role': 'user', 'content': prompt}
        ]
        response = self.generate_response(prompt)
        return response
    

def extract_keywords(text: str) -> str:
    """
    Extracts key phrases from the given text using an LLM.

    :param text: str, the text from which to extract key phrases
    :return: str, extracted key phrases
    """
    agent = OpenAIClient(
        system_prompt="You are an advanced NLP model tasked with identifying and extracting the most important and relevant key phrases from a given text. Your goal is to provide a concise list of these phrases that capture the essence of the text."
    )
    output = agent.get_output(
        prompt=f"Please analyze the following text and extract the key phrases:\n\n{text}"
    )
    return output


def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of the provided text using an LLM.

    :param text: str, the text to analyze for sentiment
    :return: str, the sentiment classification (Positive, Neutral, Negative)
    """
    agent = OpenAIClient(
        system_prompt="You are a highly capable sentiment analysis model designed to accurately classify the emotional tone of text into positive, neutral, or negative categories. Your task is to read a given piece of text, understand its emotional context, and succinctly classify the sentiment."
    )
    output = agent.get_output(
        prompt=f"Given the following text, please determine if the overall sentiment is Positive, Neutral, or Negative.\n\n{text}"
    )
    return output


def aggregate_data(keywords_list: List[str], sentiments_list: List[str]) -> Dict[str, Dict[str, int]]:
    """
    Aggregates keywords and their associated sentiments into a dictionary.

    :param keywords_list: list of lists of str, each sublist contains keywords from a single document
    :param sentiments_list: list of str, each item is the sentiment associated with a document
    :return: dict, a dictionary with keywords as keys and a sub-dictionary as values containing counts and sentiment counts
    """
    aggregate = {}
    for keywords, sentiment in zip(keywords_list, sentiments_list):
        for keyword in keywords:
            if keyword not in aggregate:
                aggregate[keyword] = {'count': 1, 'positive': 0, 'neutral': 0, 'negative': 0}
            else:
                aggregate[keyword]['count'] += 1
            if sentiment.lower() == 'positive':
                aggregate[keyword]['positive'] += 1
            elif sentiment.lower() == 'neutral':
                aggregate[keyword]['neutral'] += 1
            elif sentiment.lower() == 'negative':
                aggregate[keyword]['negative'] += 1
    return aggregate


# Example usage
if __name__ == "__main__":
    texts = ["The new market trend is shifting rapidly due to recent tech advancements.", 
             "Many are concerned about the potential downturn in market growth."]
    keywords_list = [extract_keywords(text) for text in texts]
    sentiments_list = [analyze_sentiment(text) for text in texts]
    aggregated_data = aggregate_data(keywords_list, sentiments_list)
    print("Aggregated Data:", aggregated_data)

