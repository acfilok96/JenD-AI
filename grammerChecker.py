import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai
from redlines import Redlines
from IPython.display import display, Markdown # , Latex, HTML, JSON


def GrammerChecker():
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro")
    
    ################################################

    container_1 = st.container(height = 350, border = False)

    with container_1:
        st.title("`Grammarly`")
        st.info("This is an AI grammer checker. Please put the phrase here for the correct grammer. Thank you!")
        
    ################################################
        
    if "messages_temp_7" not in st.session_state:
        st.session_state.messages_temp_7 = []

    with container_1:
        for message in st.session_state.messages_temp_7:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html = True)

    if prompt := st.chat_input("Paste your phrase here!"):
        st.session_state.messages_temp_7.append({"role": str("Grammer")+"user", "content": prompt})
        with container_1:
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                with st.spinner(":blue[Processing your response...]"):
                    msg = st.toast('Gathering information...')
                    time.sleep(0.01)
                    msg.toast('Generating...')
                    time.sleep(0.01)
                    msg.toast('Ready to go!', icon = "🥞")
                    temp_full_response = ''
                    try: 
                        full_response = ""
                        prompt_s = PromptCls.GrammerCheckPromptStyle(prompt)
                        response = model.generate_content(prompt_s)
                        diff = Redlines(prompt, response.text)
                        corrected_output = diff.output_markdown
                        
                        for i in corrected_output:
                            temp_full_response += i
                            message_placeholder.markdown(temp_full_response + "▌", unsafe_allow_html = True)
                            time.sleep(0.01)
                        message_placeholder.markdown(temp_full_response, unsafe_allow_html = True)
                    except Exception as e:
                        full_response = Excuses.listofExcuses()
                        temp_full_response = ''
                        for i in full_response:
                            temp_full_response += i
                            message_placeholder.markdown(temp_full_response + "▌", unsafe_allow_html = True)
                            time.sleep(0.01)
                        message_placeholder.markdown(full_response, unsafe_allow_html = True)
                    st.warning("Done!")
            st.session_state.messages_temp_7.append({"role": "assistant", "content": temp_full_response})
