import streamlit as st
from transformers import pipeline
import tensorflow as tf

input_text = input("Enter the text you want to summarize: ")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

if input_text:
    # Generate summary
    title = summarizer(input_text, max_length=6, min_length=2, do_sample=False)
    print("Summary: ")
    print(title[0]['summary_text'], end='...\n')
else:
    st.warning("Please enter some text to summarize.")

