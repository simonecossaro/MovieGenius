import pandas as pd
import MovieRecommendationSystem as mr
import streamlit as st


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
