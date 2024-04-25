import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai


def PythonCoding():
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro")
    
    ################################################
    container_1 = st.container(height = 350, border = False)

    with container_1:
        st.title("`Python Coder`")
        st.info("This is an AI python coder. Put your subject of code or code snippet here. Thank you!")
    
    ################################################
        
    if "messages_temp_16" not in st.session_state:
        st.session_state.messages_temp_16 = []

    

    with container_1:
        for message in st.session_state.messages_temp_16:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html = True)

    if prompt := st.chat_input("Enter the subject!"):
        st.session_state.messages_temp_16.append({"role": str("Python")+"user", "content": prompt})
        with container_1:
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                msg = st.toast('Gathering information...')
                time.sleep(0.01)
                msg.toast('Generating...')
                time.sleep(0.01)
                msg.toast('Ready to go!', icon = "🥞")
                try: 
                    full_response = ""
                    prompt = PromptCls.PythonCodingPromptStyle(prompt)
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
            st.session_state.messages_temp_16.append({"role": "assistant", "content": full_response})
