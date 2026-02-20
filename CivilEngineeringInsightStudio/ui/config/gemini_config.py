import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def configure_gemini():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
