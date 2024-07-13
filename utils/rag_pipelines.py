import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from llama_index import SimpleNode
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Initialize Pinecone
pinecone.init(api_key='your-pinecone-api-key', environment='your-environment')
index_name = 'rag-index'

# Define the vector store
embeddings = OpenAIEmbeddings()
vector_store = Pinecone(index_name=index_name, embeddings=embeddings)

# Assume documents is a list of your documents
documents = [
    {"id": "1", "text": "Document text 1"},
    {"id": "2", "text": "Document text 2"},
    # Add more documents as needed
]

# Index the documents
for doc in documents:
    node = SimpleNode(id=doc["id"], text=doc["text"])
    vector_store.add_document(node)

# Create the LangChain retrieval chain
llm = OpenAI(api_key='your-openai-api-key')
qa_chain = RetrievalQA(llm=llm, retriever=vector_store.as_retriever())

# Query the RAG system
query = "What is the information in document 1?"
response = qa_chain.run(query)
print(response)
