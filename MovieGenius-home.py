import streamlit as st

st.set_page_config(page_title="MovieGenius")

def recommendationpage():
    st.write('Film raccomandati')
    b3 = st.button('exit')
    

mood_list = ["laugh", "cry","love","adventure","fear","adrenaline","fantasy","science fiction","random"]

placeholder = st.empty()

with placeholder.container():
  st.write(f'''
                 <h1> Movie Genius </h1><h2> </h2>
             ''' , unsafe_allow_html=True)
  st.radio( "Are you an adult or a child?" , ["adult", "child"], key="qwerty")
  b = st.button('Next')

  if (b and st.session_state.qwerty == "child"):
   st.text_input('Here you can name a movie similar to the one you want to watch (*optional*)', key="zxcvbn")                   
   st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
   b1 = st.button('Go to recommendations')
   
  if (b and st.session_state.qwerty == "adult"):
   st.radio( "What do you want to feel by watching the movie?" , mood_list, key="asdfgh")
   st.text_input('Here you can name a movie similar to the one you want to watch (*optional*)', key="zxcvbn")            
   st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
   b1 = st.button('Go to recommendations')

   if b1:
      recommendationpage()
      
    
  

    
    

                     
                      
                
        
        
           

    

    
