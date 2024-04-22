from transformers import pipeline
import streamlit as st

# create a sidebar for this app that contains hyperlinks to other pages
st.sidebar.title("Try other models:")

with st.sidebar:
    st.link_button("Text Summarizer 📚", "https://simple-nlp.herokuapp.com/")
    # st.link_button("Home", "https://simple-nlp.herokuapp.com/")
    # st.link_button("Home", "https://simple-nlp.herokuapp.com/")
    # st.link_button("Home", "https://simple-nlp.herokuapp.com/")

st.title("Text Summarizer")
st.write("This app summarizes the input text using Hugging Face's transformers library. It uses the pipeline API for summarization.")

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

text = st.text_area("Enter text to summarize")
if st.button("Generate"):
    if text:
        # summarize the text
        summary = summarizer(text)
        # display the summary
        st.write(summary[0]["summary_text"])
