import pandas as pd
import MovieRecommendationSystem as mr
import streamlit as st
import DatasetInspection as di
import numpy as np


st.write('Recommended movies')

values = st.experimental_get_query_params()["qwerty"][0]


list1 = values.split('/?')

child = list1[0].replace("qwerty=", "")
mood = list1[1].replace("asdfgh=", "")
film_target = list1[2].replace("zxcvbn=", "").replace("%20", " ")
time = list1[3].replace("time=", "")

st.write(child)
st.write(mood)
st.write(film_target)
st.write(time)

for_kids = False
if (child == 'child'):
  for_kids = True
  
m = mrs.MovieRecommendationSystem()
recommended = m.recommend(for_kids, mood, film_target , Tmax )

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
