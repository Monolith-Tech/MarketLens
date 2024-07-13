# chatbot.py
# Handles chatbot functionality using OpenAI's API.

import openai

# Initialize your OpenAI API key
openai.api_key = 'your-openai-api-key'

def generate_response(query, context):
    """
    Generates a response to the user query using OpenAI's API, integrating context data.

    :param query: str, the user's question about market trends.
    :param context: str, aggregated data transformed into a readable format to inform the model.
    :return: str, the model's response, providing insights based on the context.
    """
    prompt = f"Given the following data on market trends: {context}\nUser: {query}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        stop=["\n", " User:", " AI:"]
    )
    return response.choices[0].text.strip()
