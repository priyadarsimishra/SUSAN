import streamlit as st
from transformers import pipeline
import tensorflow as tf

input_text = input("Enter the text you want to summarize: ")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

if input_text:
    # Generate summary
    summary = summarizer(input_text, max_length=100, min_length=50, do_sample=False)
    print("Summary: ")
    print(summary[0]['summary_text'])
else:
    st.warning("Please enter some text to summarize.")