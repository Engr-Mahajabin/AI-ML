# import streamlit as st

# import google.generativeai as genai

# import os
# from dotenv import load_dotenv
# load_dotenv()

# api_key = os.environ.get("Gemini_api_key")
# client = genai.Client(api_key = api_key)
# response = client.models.generative_content(
#     model = "gemini-3-flash-preview",
#     contents="Give me an idea of Gemini API in 100 words"
# )
# print(response.text)
# st.markdown(response.text)



import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found!")
else:
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-3-flash-preview")

    response = model.generate_content(
        "Give me an idea of Gemini API in 100 words"
    )

    st.title("Gemini AI Response")
    st.write(response.text)