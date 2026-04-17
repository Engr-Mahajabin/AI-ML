# Practice Day-6.5:

import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_APP")

# Init client
client = genai.Client(api_key=api_key)

# UI
st.title("Professional Sentence Improver")
st.divider()

# Input
sentence = st.text_area("Enter your sentence:")

# Button
if st.button("Improve Sentence"):
    if sentence:
        try:
            prompt = f"Improve this sentence professionally: {sentence}"

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )

            st.success("Improved Version:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a sentence first")