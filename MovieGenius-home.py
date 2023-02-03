import streamlit as st

st.set_page_config(page_title="MovieGenius")

def recommendationpage():
    st.write('Film raccomandati')
    b3 = st.button('exit')
    

mood_list = ["laugh", "cry","love","adventure","fear","adrenaline","fantasy","science fiction","random"]

c = 0
for i in range(3):
    placeholder.empty()
    with placeholder.container():
        if i == 0:
            st.write(f'''
                 <h1> Movie Genius </h1><h2> </h2>
             ''' , unsafe_allow_html=True)
            st.radio( "Are you an adult or a child?" , ["adult", "child"], key="qwerty")
            b = st.button('Next')
            if (b and st.session_state.qwerty == "child"):
                c = 2
                st.write('Ciao bambino')
            if (b and st.session_state.qwerty == "adult"):
                c = 1
                st.write('Ciao adulto')
         if (i==1 and c = 1):
            st.radio( "What do you want to feel by watching the movie?" , mood_list, key="asdfgh")
            st.text_input('Here you can name a movie similar to the one you want to watch (*optional*)', key="zxcvbn")            
            st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
            b1 = st.button('Go to recommendations')
            if (b1):
                st.write('Stiamo caricando le raccomandazioni')
         if (i==1 and c = 2):
            st.text_input('Here you can name a movie similar to the one you want to watch (*optional*)', key="zxcvbn")                   
            st.radio("How much time do you have?", ["infinite","limited"], key="minutes")
            b1 = st.button('Go to recommendations')
            if (b1):
                st.write('Stiamo caricando le raccomandazioni')
         if (i ==2):
            st.write('le raccomandazioni sono....')
            if st.button('Exit'):
                break
            
            
  

 


      
    
  

    
    

                     
                      
                
        
        
           

    

    
