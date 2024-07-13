import streamlit as st
from utils.researcher import scrape_market_data, analyze_market_trends
from utils.rag_pipelines import retrieve_and_generate
from utils.reports import generate_report, save_report
from utils.chatbot import get_chatbot_response

st.set_page_config(page_title="Market Analysis App", layout="wide")


def main():
    st.sidebar.image('assets/logo.png', width=250)
    st.sidebar.title("Market Analysis App")

    st.title("Market Analysis Dashboard")

    menu = ["Market Research", "Trends Analysis",
            "Report Generation", "Chatbot"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Market Research":
        st.subheader("Market Research")
        url = st.text_input("Enter URL to scrape")
        if st.button("Scrape Data"):
            data = scrape_market_data(url)
            st.write(data)

    elif choice == "Trends Analysis":
        st.subheader("Trends Analysis")
        query = st.text_input("Enter your query")
        documents = st.text_area("Enter documents (one per line)")
        documents_list = documents.split("\n")
        if st.button("Analyze Trends"):
            trends = analyze_market_trends(documents_list)
            st.write(trends)

    elif choice == "Report Generation":
        st.subheader("Generate Report")
        data = st.text_area("Enter data")
        trends = st.text_area("Enter trends")
        if st.button("Generate Report"):
            report = generate_report(data, trends)
            save_report(report, "market_report.txt")
            st.success("Report generated successfully!")

    elif choice == "Chatbot":
        st.subheader("Chat with our AI")
        user_input = st.text_input("You: ")
        if st.button("Send"):
            response = get_chatbot_response(user_input)
            st.write(f"Bot: {response}")


if __name__ == "__main__":
    main()
