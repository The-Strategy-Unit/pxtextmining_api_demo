import streamlit as st
import requests

st.title('Welcome to the pxtextmining API tester')

st.write('This page will allow you to query the pxtextmining API without any coding knowledge. Enter any text comment and see what labels the current model would apply to your text!')

response = requests.get(st.secrets["API_URL"])
st.write(response.json())

comment_text = st.text_input('Please enter the comment text to be labelled', value="The nurses were lovely but it was difficult to find parking")
question_type = st.selectbox('What is the type of FFT question?', ('What did we do well?', 'What could we improve?', 'Mixed or nonspecific question') )


endpoint = f"{st.secrets['API_URL']}/predict_multilabel"
