import streamlit as st
import requests
from string import punctuation

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

docs_dict = {'Gratitude/ good experience': 'General',
 'Negative experience': 'General',
 'Not assigned': 'General',
 'Organisation & efficiency': 'General',
 'Funding & use of financial resources': 'General',
 'Collecting patients feedback': 'General',
 'Non-specific praise for staff': 'Staff',
 'Non-specific dissatisfaction with staff': 'Staff',
 'Staff manner & personal attributes': 'Staff',
 'Number & deployment of staff': 'Staff',
 'Staff responsiveness': 'Staff',
 'Staff continuity': 'Staff',
 'Competence & training': 'Staff',
 'Unspecified communication': 'Communication & involvement',
 'Staff listening, understanding & involving patients': 'Communication & involvement',
 'Information directly from staff during care': 'Communication & involvement',
 'Information provision & guidance': 'Communication & involvement',
 'Being kept informed, clarity & consistency of information': 'Communication & involvement',
 'Service involvement with family/ carers': 'Communication & involvement',
 'Patient contact with family/ carers': 'Communication & involvement',
 'Contacting services': 'Access to medical care & support',
 'Appointment arrangements': 'Access to medical care & support',
 'Appointment method': 'Access to medical care & support',
 'Timeliness of care': 'Access to medical care & support',
 'Supplying & understanding medication': 'Medication',
 'Pain management': 'Medication',
 'Diagnosis & triage': 'Patient journey & service coordination',
 'Referals & continuity of care': 'Patient journey & service coordination',
 'Admission': 'Patient journey & service coordination',
 'Length of stay/ duration of care': 'Patient journey & service coordination',
 'Discharge': 'Patient journey & service coordination',
 'Care plans': 'Patient journey & service coordination',
 'Patient records': 'Patient journey & service coordination',
 'Impact of treatment/ care': 'Patient journey & service coordination',
 'Links with non-NHS organisations': 'Patient journey & service coordination',
 'Food & drink provision & facilities': 'Food & diet',
 'Feeling safe': 'TBC',
 'Patient appearance & grooming': 'TBC',
 'Equality, Diversity & Inclusion': 'TBC',
 'Activities & access to fresh air': 'Activities',
 'Electronic entertainment': 'Activities',
 'Cleanliness, tidiness & infection control': 'Environment & equipment',
 'Sensory experience': 'Environment & equipment',
 'Environment & Facilities': 'Environment & equipment',
 'Safety & security': 'Environment & equipment',
 'Provision of medical equipment': 'Environment & equipment',
 'Mental Health Act': 'Mental Health specifics',
 'Service location': 'Service location, travel & transport',
 'Transport to/ from services': 'Service location, travel & transport',
 'Parking': 'Service location, travel & transport'}

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
        if each != 'Labelling not possible':
            main_cat = docs_dict[each]
            main_cat = main_cat.lower()
            for p in punctuation:
                main_cat = main_cat.replace(p, '')
            main_cat_split = main_cat.split()
            docs_main_cat = '-'.join(main_cat_split)
            st.write(f"[{each}]({docs_url}{docs_main_cat})")
        else:
            st.write(f"{each}")
    st.balloons()
