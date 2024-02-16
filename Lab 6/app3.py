# Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import os

# Load environment variables
load_dotenv()

# Configure Google Generative AI
import google.generativeai as genai
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get response
def get_gemini_response(question, image=None, model_type='gemini-pro'):
    model = genai.GenerativeModel(model_type)
    if image:
        if question!="":
            return model.generate_content([question, image]).text
        else:
            return model.generate_content(image).text
    else:
        return model.generate_content(question).text




# Define text_to_text
def text_to_text(get_gemini_response):
    st.header("Gemini Application")
    input_text = st.text_input("Input: ", key="input")
    submit = st.button("Ask Gemini")
    if submit and input_text!="": 
        response = get_gemini_response(input_text)
        st.subheader("Response:")
        st.write(response)





# Define image_to_text
def image_to_text(get_gemini_response):
    st.header("Gemini Application")
    input_text = st.text_input("Input Prompt: ", key="input")
    uploaded_file = st.file_uploader("Choose an image")
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
    submit = st.button("Ask Gemini")
    if submit and uploaded_file is not None:
        response = get_gemini_response(input_text, image,"gemini-pro-vision")
        st.subheader("Response")
        st.write(response)

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Application")

# Sidebar to select model
model_type = st.sidebar.selectbox("Select Model", ["Text to Text Model", "Image to Text Model"])

# Display corresponding app based on model selection
if model_type == "Text to Text Model":
    text_to_text(get_gemini_response)
else:
    image_to_text(get_gemini_response)
