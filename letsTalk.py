import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai



def LetsTalk():
    
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro")
    ################################################
    container_1 = st.container(height = 350, border = False)

    with container_1:
        st.title("`Let's talk . . .`")
        st.info("This is an personal AI chatbot. Please feel free to ask any query for the helpful and friendly response. Thank you!")
    ################################################
        
    if "messages_temp_12" not in st.session_state:
        st.session_state.messages_temp_12 = []

    

    with container_1:
        for message in st.session_state.messages_temp_12:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html = True)

    if prompt := st.chat_input("Ask me anything!"):
        st.session_state.messages_temp_12.append({"role": str("Let's talk")+"user", "content": prompt})
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
                    prompt = PromptCls.ConversationPromptStyle(prompt)
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
            st.session_state.messages_temp_12.append({"role": "assistant", "content": full_response})
