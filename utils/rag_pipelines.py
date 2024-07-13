from transformers import pipeline

def retrieve_and_generate(query, documents):
    retriever = pipeline('retrieval', model='distilbert-base-uncased')
    generator = pipeline('text-generation', model='gpt-3')
    
    retrieved_docs = retriever(query, documents)
    generated_text = generator(retrieved_docs)
    return generated_text
