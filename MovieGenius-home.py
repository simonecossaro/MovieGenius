import streamlit as st

st.set_page_config(page_title="Movie recommendation")

placeholder = st.empty()

with placeholder.container():
  st.write(f'''
                 <h1> Movie recommendation App </h1><h2> Let's start with your age </h2>
             ''' , unsafe_allow_html=True)
  st.radio( "Are you an adult or a child?" , ["adult", "child"], key="qwerty")
  if st.session_state.qwerty == "child":
    placeholder.empty()
    st.write('Ciao bambino')
