import streamlit as st
import MovieRecommendationSystem as mr
import DatasetInspection as di
import pandas as pd
import numpy as np
import base64

############################# REDIRECT TO PAGE  ############################
def nav_to(url):
    nav_script = """
                    <meta http-equiv="refresh" content="0; url='%s'">
                 """ % (url)
    st.write(nav_script, unsafe_allow_html=True)
    
############################################################################
def checkInputUser(title):
        if di.checkTitolo(title) or title=="":
            st.write("You  would like to see a movie similar to: ", title)
        else:

            mystring = ", ".join(di.forseCercavi(title))

            st.write(":warning: Incorrect title! You might looked for: ", mystring)

############################################################################
def checkInputUserBoolean(title):
        if di.checkTitolo(title) or title=="":
            return True
        return False
############################################################################
def goToPage(mood, movie, time):
            if time =="limited":
                st.slider('Select maximum minutes', 0, 360, 0, key="number" )
                
                if checkInputUserBoolean(movie)==False :
                        rec_botton = st.write(f'''
                                             <div class="div">
                                                 <center>
                                                         <button  disabled="disabled"> Go to prediction movies </button>
                                                 </center>
                                             <div class="btn">
                                            ''', unsafe_allow_html=True)
                else:
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
                if checkInputUserBoolean(movie)==False :
                        rec_botton = st.write(f'''
                                             <div class="div">
                                                 <center>
                                                         <button  disabled="disabled"> Go to prediction movies </button>
                                                 </center>
                                             <div class="btn">
                                            ''', unsafe_allow_html=True)
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
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#function to set the background
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
                    <style>
                        .stApp {
                            background-image: url("data:image/png;base64,%s");
                            background-size: cover;
                        }
                    </style>
                  ''' % (bin_str)
    st.markdown(page_bg_img, unsafe_allow_html=True)
############################################################################

st.set_page_config(page_title="🎬 Movie Genius", page_icon="🎬")

set_background('cinema-bg.png')

            
mood_list = ["laugh", "cry","love","adventure","fear","adrenaline","fantasy","science fiction","random"]

placeholder = st.empty()
with placeholder.container():
    st.write(f'''
           <h1> Movie Genius 🎬</h1><h2> </h2>
          ''' , unsafe_allow_html=True)
    st.radio( "Are you an adult or a child?" , ["child", "adult"], key='qwerty')
    if (st.session_state.qwerty == "child"):
        st.text_input('Which movie is similar to the one you want to watch? (*optional*)', key="zxcvbn")
        checkInputUser(st.session_state.zxcvbn)
        st.session_state["asdfgh"] = None
        st.radio("How much time do you have?", ["infinite","limited"], key="time")
    else:
        st.radio('Which emotion would you like to feel?', mood_list, key="asdfgh")
        st.text_input('Which movie is similar to the one you want to watch? (*optional*)', key="zxcvbn")
        checkInputUser(st.session_state.zxcvbn)
        st.radio("How much time do you have?", ["infinite","limited"], key="time")
    
    goToPage(st.session_state.asdfgh, st.session_state.zxcvbn, st.session_state.time)
   
                        

     
