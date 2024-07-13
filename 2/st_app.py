import streamlit as st
import os

# Function to save uploaded file to server
def save_uploaded_file(uploaded_file):
    save_path = os.path.join("data", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

# Function to process user query
def process_query(query):
    from rag import get_response, index
    response = get_response(query=query, index=index)
    return response

# Streamlit app layout
st.set_page_config(page_title="RAG Application", page_icon="🔍", layout="wide")
st.title("📄 RAG Based Application")
st.markdown(
    """
    Welcome to the RAG-based application. This tool allows you to upload a file, 
    input a query, and get a generated response based on the file contents.
    """
)

# File upload
st.sidebar.header("Upload your file")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt", "pdf", "docx", "csv"])

if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)
    st.sidebar.success(f"File uploaded and saved to {file_path}")

# User query input
st.header("Enter your query")
query = st.text_area("Type your query here...", height=150)

if st.button("Submit Query"):
    if uploaded_file is not None and query:
        response = process_query(query)
        st.markdown("### Response")
        st.write(response)
    else:
        st.error("Please upload a file and enter a query to proceed.")

# Styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
    }
    .stTextArea>label {
        font-size: 18px;
    }
    .stTextInput>label {
        font-size: 18px;
    }
    .stMarkdown {
        font-size: 18px;
    }
    .css-1d391kg {
        font-size: 20px;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True
)
