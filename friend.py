import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai


def Friend():
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro")
    
    ################################################
    container_1 = st.container(height = 350, border = False)

    with container_1:
        st.title("`Angelina😊`")
        st.info("Hey, how are you 😊? well, you can spent some time here! have a nice day!")
    
    ################################################
        
    if "messages_temp_F" not in st.session_state:
        st.session_state.messages_temp_F = []


    with container_1:
        for message in st.session_state.messages_temp_F:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html = True)
            
    if prompt := st.chat_input("Hey, friend!"):
        st.session_state.messages_temp_F.append({"role": str("Friend")+"user", "content": prompt})
        with container_1:
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                msg = st.toast('Thinking . . .', icon = "🤔")
                time.sleep(3)
                msg.toast('Typing . . .',  icon = "👩‍💻")
                time.sleep(2)
                msg.toast('Message arrived!', icon = "💌")
                # st.snow()
                try: 
                    full_response = ""
                    prompt = PromptCls.FriendlyConversationPromptStyle(prompt)
                    response = model.generate_content(prompt, generation_config={"temperature": 0.3})
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
            st.session_state.messages_temp_F.append({"role": "assistant", "content": full_response})
