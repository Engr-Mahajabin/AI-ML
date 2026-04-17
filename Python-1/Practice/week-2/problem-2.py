# Practice Day-6.5:

import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_APP")

# Client init
client = genai.Client(api_key=api_key)

# UI
st.title("Gemini AI App")
st.divider()

# Input
prompt = st.text_area("Enter your prompt:")

# Button
if st.button("Generate Response"):
    if prompt:
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",  
                contents=prompt           
            )

            st.success(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt first")