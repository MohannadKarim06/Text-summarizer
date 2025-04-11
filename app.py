import streamlit as st

from summarizer import summarize_text

st.title("Text Summarization Tool")
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
input_text = st.text_area("Or paste your text here:", height=200)

max_length = st.slider("Max Length", 50, 300, 130)
min_length = st.slider("Min Length", 10, 100, 30)
length_penalty = st.slider("Length Penalty", 0.5, 2.5, 2.0)
summary = ""

if st.button("Summarize"):
     
     if uploaded_file:  
       input_text =  uploaded_file.read().decode("utf-8")
     if input_text:
         try:
            if len(input_text.split()) > 512:
               st.error("Input text is too long. Please limit it to 512 tokens")
            elif len(input_text.split()) < 50:
               st.error("The input text is too short for accurate summarization. Please enter more text.")
            else:  
               summary = summarize_text(input_text, max_length=max_length, min_length=min_length, length_penalty=length_penalty)
         except Exception as e:
            st.error(f"an error occurred: {str(e)}")  
         st.subheader("Summary:")
         st.write(summary)

     else:
        st.warning("Please provide some text to summarize.")         


st.download_button("Download Summary", summary, file_name="summary.txt")