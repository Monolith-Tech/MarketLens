import tiktoken
from llama_index.core import set_global_service_context
from llama_index.core import VectorStoreIndex
from llama_index.core import PromptHelper
from llama_index.core import ServiceContext
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.text_splitter import TokenTextSplitter, SentenceSplitter
from llama_index.core import SimpleDirectoryReader

import os
from dotenv import load_dotenv
load_dotenv()


# document loaders
documents = SimpleDirectoryReader(input_dir='data').load_data()

# Creating Text Chunks
text_splitter = TokenTextSplitter(
    separator=" ",
    chunk_size=1024,
    chunk_overlap=20,
    backup_separators=["\n"],
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)

# node parser
node_parser = SimpleNodeParser.from_defaults(
    text_splitter=TokenTextSplitter
)

# # sentence splitter
# text_splitter = SentenceSplitter(
#     separator=" ",
#     chunk_size=1024,
#     chunk_overlap=20,
#     paragraph_separator="\n\n\n",
#     secondary_chunking_regex="[^,.;。]+[,.;。]?",
#     tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
# )

# embedding
embed_model = OpenAIEmbedding()

# llm
llm = OpenAI(model='gpt-3.5-turbo', temperature=0, max_tokens=256)

prompt_helper = PromptHelper(
    context_window=4096,
    num_output=256,
    chunk_overlap_ratio=0.1,
    chunk_size_limit=None
)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    node_parser=node_parser,
    prompt_helper=prompt_helper
)

# index
index = VectorStoreIndex.from_documents(
    documents=documents,
    service_context=service_context
)

# query engine
query_engine = index.as_query_engine(service_context=service_context)
response = query_engine.query("who is madhav?")
print(response)