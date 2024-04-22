from transformers import pipeline
import streamlit as st
from st_pages import Page, add_page_title, show_pages


show_pages(
    [
        Page("summarize.py", "Text Summarizer", "📚"),
        Page("qa.py", "Question Answering System", "❓"),
        Page("generate.py", "Text Generator (GPT-2)", "📝"),
        Page("translate.py", "Text Translator (English to French)", "🇫🇷"),
        Page("sentiment.py", "Sentiment Analysis", "😊"),
    ]
)

st.title("Text Summarizer")
st.write("This app summarizes the input text using Hugging Face's transformers library. It uses the pipeline API for summarization.")

summarizer = pipeline("summarization")

text = st.text_area("Enter text to summarize")
if st.button("Generate"):
    if text:
        # summarize the text
        summary = summarizer(text, min_length=5, max_length=30)
        # display the summary
        st.write(summary[0]["summary_text"])
