import streamlit as st
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

#create a titile 
st.title("Langchain openai chatbot")
open_api_key = st.sidebar.text_input("please enter your open API KEY", type="password")

def generate_response(input_text):
    llm=OpenAI(temperature=0.8, openai_api_key=open_api_key)
    st.info(llm.invoke(input_text))

with st.form("myform"):
    text = st.text_area("Enter your text ", "What Questions would you like to ask ")
    submitted = st.form_submit_button("Submit")
    if not open_api_key.startswith('sk-'):
        st.warning("Please enter a valid key")
    if submitted and open_api_key.startswith('sk-'):
        generate_response(text)
