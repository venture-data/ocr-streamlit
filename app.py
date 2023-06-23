import streamlit as st
from PIL import Image
import pytesseract


def extract_text(image):
    # Extract text from the image using Pytesseract
    text = pytesseract.image_to_string(image)
    return text


st.title("Image to Text Converter")

# Allow the user to upload an image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image file using PIL
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text from the uploaded image
    text = extract_text(image)

    # Display the extracted text
    st.write("Extracted Text:")
    st.write(text)