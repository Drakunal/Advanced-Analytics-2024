import streamlit as st
from PyPDF2 import PdfReader
import os
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS
from io import BytesIO

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))





#function for getting text from the pdf files
def get_text_from_pdf(pdf_file):
    text=""
    for pdf in pdf_file:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text


#function for splitting text into chunks of data
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


#saving of the text in the form of embeddings in a vector database  file
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


#Prompt template for langchain
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, 
    make sure to provide all the details, if the answer is not in
    provided context just say, 
    "Answer is not available in the context", 
    don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=1)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain


#response based on the user input and the value from vector database
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    # print(response)
    sound_file = BytesIO()
    tts = gTTS(response["output_text"], lang='en')
    tts.write_to_fp(sound_file)
    st.audio(sound_file)
    st.write("Reply: ", response["output_text"])




#frontend portion
def main():
    st.set_page_config("PDF Easy!")
    st.header("🧙🏻Listen and Chat with PDFs!!🧙🏻")

    user_question = st.text_input("Ask anything related to the document")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_text_from_pdf(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")



if __name__ == "__main__":
    main()