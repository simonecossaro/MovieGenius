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
def goToPage(mood, movie, time):
            if time =="limited":
                st.slider('Select maximum minutes', 0, 360, 0, key="number" )
                
                rec_botton = st.write(f'''
                                             <div class="div">
                                                 <center>
                                                     <a href="https://simonecossaro-moviegenius-output-mv1sij.streamlit.app/?qwerty=%s/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                                         <button> Go to prediction movies </button>
                                                     </a>
                                                 </center>
                                             <div class="btn">
                                            ''' % (st.session_state.qwerty, mood, movie, st.session_state.number), unsafe_allow_html=True)
     
            else:
                rec_botton = st.write(f'''
                                             <div class="div">
                                                 <center>
                                                     <a href="https://simonecossaro-moviegenius-output-mv1sij.streamlit.app/?qwerty=%s/?asdfgh=%s/?zxcvbn=%s/?time=%s">
                                                         <button> Go to prediction movies </button>
                                                     </a>
                                                 </center>
                                             <div class="btn">
                                            ''' % (st.session_state.qwerty,mood, movie , 600), unsafe_allow_html=True)
            
            if rec_botton :
                        nav_to("https://simonecossaro-moviegenius-output-mv1sij.streamlit.app")
                    
############################################################################
st.set_page_config(page_title="MovieGenius")

            
mood_list = ["laugh", "cry","love","adventure","fear","adrenaline","fantasy","science fiction","random"]

placeholder = st.empty()
with placeholder.container():
    st.write(f'''
           <h1> Movie Genius </h1><h2> </h2>
          ''' , unsafe_allow_html=True)
    st.radio( "Are you an adult or a child?" , ["adult", "child"], key='qwerty')
    st.radio('Which emotion would you like to try?', mood_list, key="asdfgh")
    st.text_input('Which movie is similar to the one you want to watch? (*optional*)', key="zxcvbn")
    st.radio("How much time do you have?", ["infinite","limited"], key="time")
    goToPage(st.session_state.asdfgh, st.session_state.zxcvbn, st.session_state.time)
   
                        

     
