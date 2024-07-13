from transformers import pipeline

chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

def get_chatbot_response(user_input):
    response = chatbot(user_input)
    return response
