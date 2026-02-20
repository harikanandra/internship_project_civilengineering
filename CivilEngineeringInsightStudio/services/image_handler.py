from PIL import Image

def process_image(uploaded_file):
    if uploaded_file is None:
        return None

    image = Image.open(uploaded_file)
    image_bytes = uploaded_file.getvalue()

    return [{
        "mime_type": uploaded_file.type,
        "data": image_bytes
    }], image
