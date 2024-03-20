from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

#Loading the api key and configuring the genai module with it
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')

## Function to load Gemini model and get responses
def get_gemini_response(input,image):
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text



##initialize streamlit app
st.set_page_config(page_title="Gemini Pro Vision")

st.header("Gemini AI Image Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Upload an image")

image=""  

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Ask Gemini")


## If ask button is clicked and file is not empty
if submit and uploaded_file is not None:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)