from transformers import pipeline
import streamlit as st

st.title("Question Answering System")
st.write("This app uses Hugging Face's transformers library to answer questions based on the given context.")

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

context = st.text_area('Enter the context here')
question = st.text_input('Enter your question here')

if st.button('Generate'):
    if question and context:
        result = qa_pipeline(question=question, context=context)
        st.write(result)
