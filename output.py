import pandas as pd
import MovieRecommendationSystem as mr


st.write('Recommended movies')

values = st.experimental_get_query_params()["qwerty"][0]
list1 = values.split('/?')

st.write(list1)
