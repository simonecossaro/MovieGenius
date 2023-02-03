import streamlit as st

st.set_page_config(page_title="MovieGenius")

def recommendationpage():
    placeholder3 = st.empty()
    with placeholder3.container():
        st.write('Film raccomandati')
        b3 = st.button('exit')
    
r = False
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
    recommendationpage()
                    
            
                

    

            
            
  

 


      
    
  

    
    

                     
                      
                
        
        
           

    

    
