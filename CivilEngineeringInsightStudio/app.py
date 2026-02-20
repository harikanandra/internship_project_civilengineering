import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# -------------------------------
# Function to get Gemini response (TEXT ONLY – STABLE)
# -------------------------------
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# -------------------------------
# Streamlit App Configuration
# -------------------------------
st.set_page_config(
    page_title="Civil Engineering Insight Studio",
    page_icon="🏗️",
    layout="centered"
)

st.header("Civil Engineering Insight Studio")

# -------------------------------
# User Inputs
# -------------------------------
input_text = st.text_input(
    "Input Prompt:",
    placeholder="Describe the civil engineering structure in detail"
)

uploaded_file = st.file_uploader(
    "Choose an image of a civil engineering structure...",
    type=["jpg", "jpeg", "png"]
)

# -------------------------------
# Display Uploaded Image
# -------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# -------------------------------
# Button
# -------------------------------
submit = st.button("Describe Structure")

# -------------------------------
# Base Prompt
# -------------------------------
base_prompt = """
You are an expert civil engineer.
Provide a detailed description of a civil engineering structure including:
- Type of structure
- Materials used
- Approximate dimensions
- Construction methods
- Notable features or engineering challenges

Assume the description is based on the uploaded image.
"""

# -------------------------------
# Generate Output
# -------------------------------
if submit:
    final_prompt = base_prompt

    if input_text.strip() != "":
        final_prompt += "\nUser Instruction: " + input_text

    try:
        response = get_gemini_response(final_prompt)
        st.subheader("Structure Description")
        st.write(response)
    except Exception as e:
        st.error(f"Error occurred: {e}")
