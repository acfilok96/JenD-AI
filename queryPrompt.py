import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai


def QueryPrompt():
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro")
    
    ################################################
    container_1 = st.container(height = 350, border = False)

    with container_1:
        st.title("`Query & Prompt`")
        st.info("Please put your query & prompt here. Thank you!")
        
        ################################################
        col1, col2 = st.columns(2)
        
        prompt = ""
        with col1:
            prompt = st.text_input(":blue[Prompt]", placeholder='Enter your prompt here . . .') # "Enter your prompt here . . ." # , key=placeholder
            
        query = ""
        with col2:
            query = st.text_input(":blue[Query]", placeholder='Enter your query here . . .') #  "Enter your query here . . ." # , key=placeholder
        
    
        
    ################################################
        if st.button("Get your response!"):
            if prompt:
                if query:
                    
                    
                    with st.chat_message("user"):
                        st.markdown(query)
                
                    with st.chat_message("assistant"):
                        with st.spinner(":green[processing response . . .]"):
                            message_placeholder = st.empty()
                            try: 
                                full_response = ""
                                prompt = PromptCls.promptQueryClash(prompt, query)
                                response = model.generate_content(prompt)
                                for responses in response.text:
                                    full_response += responses
                                    message_placeholder.markdown(full_response + "▌")
                                    time.sleep(0.01)
                                message_placeholder.markdown(full_response)
                            except Exception as e:
                                full_response = Excuses.listofExcuses()
                                temp_full_response = ''
                                for i in full_response:
                                    temp_full_response += i
                                    message_placeholder.markdown(temp_full_response + "▌")
                                    time.sleep(0.01)
                                message_placeholder.markdown(full_response)
