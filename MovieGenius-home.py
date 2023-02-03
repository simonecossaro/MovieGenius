import streamlit as st

st.set_page_config(page_title="MovieGenius")

placeholder = st.empty()

with placeholder.container():
  st.write(f'''
                 <h1> Movie Genius </h1><h2> </h2>
             ''' , unsafe_allow_html=True)
  st.radio( "Are you an adult or a child?" , ["adult", "child"], key="qwerty")
  b = st.button('Next')
  
if (b and st.session_state.qwerty == "child"):
    placeholder.empty()
    placeholder1 = st.empty()
    with placeholder1.container():
      st.write('Hello child')
    
if (b and st.session_state.qwerty == "adult"):
    placeholder.empty()
    placeholder2 = st.empty()
    with placeholder2.container():
      st.write('Hello adult')
           

    

    
