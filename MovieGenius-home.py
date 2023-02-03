import streamlit as st
import MovieRecommendationSystem as mr
import DatasetInspection as di
import pandas as pd
import numpy as np

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
    placeholder.empty()
    for_child = False
    if (st.session_state['tipo'] == 'child'):
            for_child = True
    tMax = 600
    if (st.session_state['time'] == "limited"):
            tMax = st.session_state['minutes']
    m = mr.MovieRecommendationSystem()
    recommended = m.recommend(for_kids, st.session_state['mood'], st.session_state['film_target'], tMax )
    listRecom = recommended['title'].values
    listOverview = []
    st.write(f'''
                 <h1> Movie recommendation App </h1><h2> Recommended movies: </h2>
             ''' , unsafe_allow_html=True)
    for i in range(len(listRecom)):
            value = di.trovaOverview(listRecom[i])
            listOverview.append(value)
    col1, col2 = st.columns(2)
    with col1:
            for i in range(0,10):
                        st.write(f'''
                                     <div > <big><b>%d -</b>  %s </big>
                                    </div>
                                    ''' % (i+1, listRecom[i]), unsafe_allow_html=True)
    with col2:
             option= st.selectbox("Read the overview of", (listRecom[0],listRecom[1],listRecom[2],listRecom[3],listRecom[4],listRecom[5],listRecom[6],
                                                     listRecom[7],listRecom[8],listRecom[9]))
             st.write(di.trovaOverview(option))
        
   
                        
         

     
