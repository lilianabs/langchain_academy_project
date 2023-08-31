import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def generate_response(txt):
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    result = llm.predict(txt)
    return result
    
st.set_page_config(page_title='🦜🔗 Vegetarian Food Advice')
st.title('🦜🔗 Vegetarian Food Advice App')


result = []
with st.form('summarize_form'):
    # Text input
    txt_input = st.text_area('Enter your text', '', height=200)
    submitted = st.form_submit_button('Submit')
    if submitted:
        with st.spinner('Calculating...'):
            response = generate_response(txt_input)
            result.append(response)

if len(result):
    st.info(response)