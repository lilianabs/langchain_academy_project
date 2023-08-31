import streamlit as st
from vegetarian_food_advice.generate_recipes import generate_response
    
st.set_page_config(page_title='🦜🔗 Vegetarian Food Advice')
st.title('🦜🔗 Vegetarian Food Advice App')

result = []
with st.form('generate_avice'):
    # Text input
    txt_input = st.text_area('Enter your text', '', height=80)
    submitted = st.form_submit_button('Generate')
    if submitted:
        with st.spinner('Calculating...'):
            response = generate_response(txt_input)
            result.append(response)

if len(result):
    st.info(response)