from transformers import pipeline
import streamlit as st

# create a streamlit app that translates english to japanese using Hugging Face's transformers library
st.title("Text Translator (English to French)")

# create a pipeline for translation
translator = pipeline("translation_en_to_fr", model='t5-small')

# create a text input for the user to enter text to translate
text = st.text_area("Enter text to translate")

# create a button to trigger the translation
if st.button("Translate"):
    if text:
        # translate the text
        translation = translator(text)
        # display the translated text
        st.write(translation[0]["translation_text"])

