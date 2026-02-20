import google.generativeai as genai

def analyze_structure(user_text, image_parts, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")

    response = model.generate_content([
        user_text,
        image_parts[0],
        prompt
    ])

    return response.text
