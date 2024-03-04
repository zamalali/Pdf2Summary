import streamlit as st
from main import read_pdf, extract_key_phrases, score_sentences, summarize_text
import io
import base64

# Initialize your Streamlit app
st.title("🚀 PDF to Bullet Point Summarizer 🗟 🔏")

# Initialize the Streamlit app


# File uploader for the PDF
uploaded_file = st.file_uploader("Upload your PDF document", type="pdf")

# Slider for users to select the summarization extent
summary_scale = st.slider("Select the extent of summarization (%)", min_value=1, max_value=100, value=20)

if uploaded_file is not None:
    with st.spinner('Processing...'):
        # Read the PDF content
        text = read_pdf(io.BytesIO(uploaded_file.getvalue()))
        
        # Extract key phrases from the text
        key_phrases = extract_key_phrases(text)
        
        # Score sentences based on the key phrases
        sentence_scores = score_sentences(text, key_phrases)
        
        # Determine the number of bullet points based on the selected summarization scale
        total_sentences = len(list(sentence_scores.keys()))
        num_points = max(1, total_sentences * summary_scale // 100)
        
        # Generate the bullet-point summary
        summary = summarize_text(sentence_scores, num_points=num_points)
        
        # Display the summary as bullet points
        st.subheader("Here's the summary 💯: ")
        st.markdown(summary)
