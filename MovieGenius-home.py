import streamlit as st

st.set_page_config(page_title="MovieGenius")

def childpage():
    placeholder3 = st.empty()
    with placeholder3.container():
        st.text_input('Here you can name a movie similar to the one you want to watch (*optional*)', key="zxcvbn")                   
        st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
        b1 = st.button('Go to recommendations')
        if b1:
            placeholder3.empty()
            recommendationpage()
            
def recommendationpage():
    placeholder4 = st.empty()
    with placeholder4.container():
        st.write('Ecco i film raccomandati')
            
mood_list = ["laugh", "cry","love","adventure","fear","adrenaline","fantasy","science fiction","random"]

st.write(f'''
           <h1> Movie Genius </h1><h2> </h2>
          ''' , unsafe_allow_html=True)

placeholder = st.empty()
with placeholder.container():
    st.radio( "Are you an adult or a child?" , ["adult", "child"], key="qwerty")
    b = st.button('Next')

if (b and st.session_state.qwerty == "child"):
    placeholder.empty()
    childpage()
                    
            
                

    

            
            
  

 


      
    
  

    
    

                     
                      
                
        
        
           

    

    
