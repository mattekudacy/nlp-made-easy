from transformers import pipeline
from st_pages import Page, add_page_title, show_pages
import streamlit as st

st.title("Text Generator (GPT-2)")
st.write("This app generates text based on the given input using Hugging Face's transformers library. It uses the pipeline API for text generation.")

text_generator = pipeline('text-generation', model="gpt2")

input_text = st.text_input("Enter your text here:")
generate_button = st.button("Generate")

if generate_button:
    generated_text = text_generator(input_text, do_sample=False)
    st.write(generated_text[0]["generated_text"])