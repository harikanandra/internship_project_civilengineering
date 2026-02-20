import streamlit as st

def render_ui():
    st.set_page_config(
        page_title="Civil Engineering Insight Studio",
        page_icon="🏗️",
        layout="centered"
    )

    st.title("🏗️ Civil Engineering Insight Studio")
    st.markdown("AI-Powered Structural Analysis System")

    text = st.text_input("Enter additional details (optional):")
    image = st.file_uploader(
        "Upload Civil Engineering Structure Image",
        type=["jpg", "jpeg", "png"]
    )

    submit = st.button("Analyze Structure")

    return text, image, submit
