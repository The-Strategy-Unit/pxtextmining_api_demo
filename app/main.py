import streamlit as st
import requests

st.title('Welcome to the pxtextmining API tester')

st.write('This page will allow you to query the pxtextmining API without any coding knowledge. Enter any text comment and see what labels the current model would apply to your text!')

question_type = st.selectbox('What is the type of FFT question?', ('Mixed or nonspecific question', 'What did we do well?', 'What could we improve?') )
if question_type == 'What did we do well?':
    st.write('Select this option if your question is similar to this. Similar questions might include "What was good?", or "Was there anything you were particularly satisfied with?"')
    q_type = 'what_good'
if question_type == 'What could we improve?':
    st.write('Select this option if your question is similar to this. Other questions might include "Is there anything we could have done better?", or "Was there anything you were dissatisfied with?"')
    q_type = 'could_improve'
if question_type == 'Mixed or nonspecific question':
    st.write('Select this option if your question is mixed, or generic. Similar questions might include "Why did you give us this answer?", or "What were you satisfied/dissatisfied with?"')
    q_type = 'nonspecific'


comment_text = st.text_input('Please enter the comment text to be labelled', value="The nurses were lovely but it was difficult to find parking.")

endpoint = f"{st.secrets['API_URL']}/predict_multilabel"
docs_url = "https://cdu-data-science-team.github.io/PatientExperience-QDC/framework/framework3.html#"


if st.button('Submit'):
    text_data = [
              { 'comment_id': '1', # The comment_id values in each dict must be unique.
                'comment_text': comment_text,
                'question_type': q_type },
            ]
    response = requests.post(endpoint,
                          json = text_data)
    prediction = response.json()[0]
    st.write("The predicted labels for your text are:")
    for each in prediction['labels']:
        st.write(each)
    st.balloons()
