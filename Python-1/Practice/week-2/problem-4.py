# Practice Day-7.5:

import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_APP")

# Init Gemini client
client = genai.Client(api_key=api_key)

# UI
st.title("🧠 AI Code Debugger App")
st.divider()

# Upload image
image_file = st.file_uploader(
    "Upload error screenshot",
    type=["png", "jpg", "jpeg"]
)

# Option bar
mode = st.selectbox(
    "Choose output type",
    ("Hints", "Solution with code")
)

# Button
if st.button("Debug Code"):

    # Validation
    if not image_file or not mode:
        st.error("⚠️ Please upload image and select mode first!")
    else:
        try:
            with st.spinner("Analyzing error with Gemini AI..."):

                prompt = ""

                if mode == "Hints":
                    prompt = """
                    Analyze this code error screenshot and give only hints to fix the issue.
                    Do NOT provide full solution.
                    """

                else:
                    prompt = """
                    Analyze this code error screenshot and provide:
                    1. Error explanation
                    2. Fixed code
                    3. Short explanation of fix
                    """

                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=[
                        {
                            "role": "user",
                            "parts": [
                                {"text": prompt},
                                {
                                    "inline_data": {
                                        "mime_type": image_file.type,
                                        "data": image_file.getvalue()
                                    }
                                }
                            ]
                        }
                    ]
                )

            st.markdown("## 🧾 Result")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")