import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai



def Education():
    
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro")
    ################################################

    container_1 = st.container(height = 350, border = False)

    with container_1:
        st.title("`Educational Query`")
        st.info("This is an educational chatbot. Feel free to ask any query for the helpful and educational response. Thank you!")
    ################################################
        
    if "messages_temp_Ed" not in st.session_state:
        st.session_state.messages_temp_Ed = []

    with container_1:
        for message in st.session_state.messages_temp_Ed:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html = True)

    if prompt := st.chat_input("Ask me anything!"):
        st.session_state.messages_temp_Ed.append({"role": str("Educational")+"user", "content": prompt})
        with container_1:
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                msg = st.toast('Gathering information...')
                time.sleep(1)
                msg.toast('Generating...')
                time.sleep(1)
                msg.toast('Response just arrived!', icon = "🥞")
                with st.spinner("Processing your response..."):
                    try: 
                        full_response = ""
                        prompt = PromptCls.EducationalPromptStyle(prompt)
                        response = model.generate_content(prompt, generation_config={"temperature": 0.2})
                        for responses in response.text:
                            full_response += responses
                            message_placeholder.markdown(full_response + "▌")
                            time.sleep(0.01)
                        message_placeholder.markdown(full_response)
                        # st.latex(response.text)
                    except Exception as e:
                        full_response = Excuses.listofExcuses()
                        temp_full_response = ''
                        for i in full_response:
                            temp_full_response += i
                            message_placeholder.markdown(temp_full_response + "▌")
                            time.sleep(0.01)
                        message_placeholder.markdown(full_response)
                    st.session_state.messages_temp_Ed.append({"role": "assistant", "content": full_response})
                st.success("Done!")
