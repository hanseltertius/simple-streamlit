from transformers import pipeline
import streamlit as st

st.title("aplikasi sederhana")
st.write("Ini adalah aplikasi sederhana")

classifier = pipeline("sentiment-analysis")

text_input = st.text_input("Insert a sentence")
if st.button("Submit"):
    result = classifier(text_input)
    st.json(result)
