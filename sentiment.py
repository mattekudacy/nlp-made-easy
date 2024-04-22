from transformers import pipeline
from st_pages import Page, add_page_title, show_pages
import streamlit as st

# create a streamlit app that performs sentiment analysis using Hugging Face's transformers library

st.title("Sentiment Analysis")
st.write("This app analyzes the sentiment of the input text using Hugging Face's transformers library. It uses the pipeline API for sentiment analysis.")

# create a pipeline for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis")

# create a text input for the user to enter text for sentiment analysis
text = st.text_area("Enter text for sentiment analysis")

# create a button to trigger the sentiment analysis
if st.button("Analyze Sentiment"):
    if text:
        # analyze the sentiment of the text
        sentiment = sentiment_analyzer(text)
        # display the sentiment analysis result
        st.write(sentiment[0])

