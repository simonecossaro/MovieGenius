import pandas as pd
import MovieRecommendationSystem as mr


st.write(f'''
                 <h1> Movie recommendation App </h1><h2> Recommended movies: </h2>
             ''' , unsafe_allow_html=True)


values = st.experimental_get_query_params()["qwerty"][0]
list1 = values.split('/?')

st.write(list1)
