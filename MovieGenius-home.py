import streamlit as st
import MovieRecommendationSystem as mr
import DatasetInspection as di
import pandas as pd
import numpy as np

############################# REDIRECT TO PAGE  ############################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
############################################################################

st.set_page_config(page_title="MovieGenius")

            
mood_list = ["laugh", "cry","love","adventure","fear","adrenaline","fantasy","science fiction","random"]

placeholder = st.empty()
with placeholder.container():
    st.write(f'''
           <h1> Movie Genius </h1><h2> </h2>
          ''' , unsafe_allow_html=True)
    st.session_state['tipo'] = st.radio( "Are you an adult or a child?" , ["adult", "child"])
    st.session_state['mood'] = st.radio('Which emotion would you like to try?', mood_list)
    st.session_state['film_target'] = st.text_input('Which movie is similar to the one you want to watch? (*optional*)')
    st.session_state['time'] = st.radio("How much time do you have?", ["infinite","limited"])
    if (st.session_state.time == "limited"):
        st.session_state['minutes'] = st.slider('Select maximum minutes', 0, 360, 0)
    b = st.button('Go to recommendations')
    
if b:
    nav_to('https://simonecossaro-moviegenius-output-mv1sij.streamlit.app')
        
   
                        
         

     
