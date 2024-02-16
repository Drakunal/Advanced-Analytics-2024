#pip install -q -U google-generativeai
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai

#Loading the api key and configuring the genai module with it
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


## Function to load Gemini model and get responses
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text



##initialize streamlit app
st.set_page_config(page_title="Gemini Application")
st.header("Gemini AI Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask Gemini.")

## If ask button is clicked and input is not empty
if submit and input!="":
    response=get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)