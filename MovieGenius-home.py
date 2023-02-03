import streamlit as st
import MovieRecommendationSystem as mr

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
    st.write(st.session_state['tipo'])
    st.write(st.session_state['mood'])
    st.write(st.session_state['film_target'])
    st.write(st.session_state['time'])
    st.write(st.session_state['minutes'])
         

     
