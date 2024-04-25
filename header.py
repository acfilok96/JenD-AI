import streamlit as st
from streamlit_option_menu import option_menu

# One
from letsTalk import LetsTalk
from medicalAssistant import MedicalAssistant
# from friend import Friend

# Two
from negativeEmails import NegativeEmails
from positiveEmails import PositiveEmails

# Three
from summarize import Summarize
from caseStudy import CaseStudy
from expand import Expand
from grammerChecker import GrammerChecker

# Four
from pythonCoding import PythonCoding
from jsonCoding import JsonCoding
from javaCoding import JavaCoding
from candcPlusPlusCoding import CandcPlusPlusCoding
from sql import SQLs 

# Five
# from csvfileAnalyzer import CsvFileAnalyzer
# from xlsxfileAnalyzer import XlsxFileAnalyzer

# Six
from quantumQuery import QuantumQuery
from quantumCoder import QuantumCoder
 
# Seven
from stockMarket import StockMarket

# Eight
from htmlCoding import HTMLCoding 
from cssCoding import CSSCoding 
from javascriptCoding import JavaScriptCoding 
from frontendCoding import FrontendCoding

# Nine
from queryPrompt import QueryPrompt
from imageDescription import ImageDescription

# Ten
from education import Education


# st.set_page_config(layout="wide")
st.set_page_config(page_title='JenD.ai', layout="wide", page_icon = 'Image1/d2.jpg', initial_sidebar_state = 'auto')

st.markdown("""
<style>
.big-font-1 {
    font-size:30px !important;
    text-align: center; 
    color: yellow
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.big-font-2 {
    font-size:23px !important;
    text-align: center;
    color: yellow
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.big-font-3 {
    font-size:13px !important;
    text-align: center;
    color: yellow
}
</style>
""", unsafe_allow_html=True)


# Page 1
def page_1():
    # horizontal menu
    # st.caption("Welcome to EY.ai")
    # st.markdown("<h3 style='text-align: center; color: white'>Welcome to <h3 sstyle='text-align: center; color: yellow'>EY.ai</h3></h3>", unsafe_allow_html=True)
    # st.markdown("<h3 style='text-align: center; color: yellow'>Let's talk . . .</h3>", unsafe_allow_html=True)
    # st.markdown("<p class='big-font-2'>. . . Let's Talk || Gemini Pro . . .</p>", unsafe_allow_html=True)
    # st.markdown("<p class='big-font-3'>||GenD.ai||</p>", unsafe_allow_html=True)
    selected_1 = option_menu(menu_title = None,
                        options=["Let's Talk", "Medico"], 
                        icons = ["chat-dots", "heart-pulse-fill"], # lungs-fill
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_1 == "Let's Talk":
        LetsTalk()
    elif selected_1 == "Medico":
        MedicalAssistant()

# Page 2
def page_2():
    # horizontal menu
    # st.markdown("<h3 style='text-align: center; color: yellow'>Writer</h3>", unsafe_allow_html=True)
    # st.markdown('<p class="big-font-2">. . . Writer || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_2 = option_menu(menu_title = None,
                        options=[ "Summarizer", "Case Study", "Novel Writer", "Grammarly"], 
                        icons = ["book", "body-text", "book-half", "search"], 
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_2 == "Summarizer":
        Summarize()
    elif selected_2 == "Case Study":
        CaseStudy()
    elif selected_2 == "Novel Writer":
        Expand()
    elif selected_2 == "Grammarly":
        GrammerChecker()

# Page 3
# def page_3():
#     # horizontal menu
#     # st.markdown("<h3 style='text-align: center; color: yellow'>File Analyzer</h3>", unsafe_allow_html=True)
#     st.markdown('<p class="big-font-2">. . . File Analyzer . . .</p>', unsafe_allow_html=True)
#     selected_3 = option_menu(menu_title = None,
#                         options=["csv", "xlsx"], 
#                         icons = ["filetype-csv","filetype-xlsx"], 
#                         menu_icon = "cast",
#                         default_index = 0,
#                         orientation = "horizontal",
#                         )
#     if selected_3 == "csv":
#         CsvFileAnalyzer()
#     elif selected_3 == "xlsx":
#         XlsxFileAnalyzer()

# Page 4       
def page_4():
    # horizontal menu
    # st.markdown("<h3 style='text-align: center; color: yellow'>Coder</h3>", unsafe_allow_html=True)
    # st.markdown('<p class="big-font-2">. . . Coder || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_4 = option_menu(menu_title = None,
                        options=["Python", "SQL", "C/C++", "java", "JSON"], 
                        icons = ["filetype-py", "database-check", "c-circle-fill", "filetype-java", "filetype-json"], # filetype-sql
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_4 == "Python":
        PythonCoding()
    elif selected_4 == "SQL":
        SQLs()
    elif selected_4 == "C/C++":
        CandcPlusPlusCoding()
    elif selected_4 == "java":
        JavaCoding()
    elif selected_4 == "JSON":
        JsonCoding()
        
        
# Page 5       
def page_5():
    # horizontal menu
    # st.markdown("<h3 style='text-align: center; color: yellow'>Email Attender</h3>", unsafe_allow_html=True)
    # st.markdown('<p class="big-font-2">. . . Email Attender || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_5 = option_menu(menu_title = None,
                        options=["Positive Email Attender", "Negative Email Attender"], 
                        icons = ["envelope-check-fill", "envelope-exclamation-fill"],   # envelope-x-fill
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_5 == "Positive Email Attender":
        PositiveEmails()
    elif selected_5 == "Negative Email Attender":
        NegativeEmails()
        
# Page 6
def page_6():
    # horizontal menu
    # st.markdown("<h3 style='text-align: center; color: yellow'>Quantumania</h3>", unsafe_allow_html=True)
    # st.markdown('<p class="big-font-2">. . . Quantumania || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_6 = option_menu(menu_title = None,
                        options=["Quantum Query", "Quantum Coder"], 
                        icons = ["hurricane", "globe"], # asterisk, hurricane, snow2, virus2 
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_6 == "Quantum Query":
        QuantumQuery()
    elif selected_6 == "Quantum Coder":
        QuantumCoder()
        
        
# Page 7
def page_7():
    # horizontal menu
    # st.markdown("<h3 style='text-align: center; color: yellow'>Stock Market</h3>", unsafe_allow_html=True)
    # st.markdown('<p class="big-font-2">. . . Stock Market || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_7 = option_menu(menu_title = None,
                        options=["Analyze Stock Market"], 
                        icons = ["kanban"], 
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_7 == "Analyze Stock Market":
        StockMarket()
        
        
# Page 8      
def page_8():
    # horizontal menu
    # st.markdown("<h3 style='text-align: center; color: yellow'>Coder</h3>", unsafe_allow_html=True)
    # st.markdown('<p class="big-font-2">. . . Web Development || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_8 = option_menu(menu_title = None,
                        options=["HTML", "CSS", "Javascript", "Frontend"], 
                        icons = ["filetype-html", "filetype-css", "filetype-js", "motherboard"], # filetype-sql
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_8 == "HTML":
        HTMLCoding()
    elif selected_8 == "css":
        CSSCoding()
    elif selected_8 == "javascript":
        JavaScriptCoding()
    elif selected_8 == "Frontend":
        FrontendCoding()
      
        
# Page 9
def page_9():
    # horizontal menu
    # st.markdown("<h3 style='text-align: center; color: yellow'>Stock Market</h3>", unsafe_allow_html=True)
    # st.markdown('<p class="big-font-2">. . . Prompt & Query || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_9 = option_menu(menu_title = None,
                        options=["Prompt & Query", "Image Description"], 
                        icons = ["kanban", "snow2"], 
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_9 == "Prompt & Query":
        QueryPrompt()
    elif selected_9 == "Image Description":
        ImageDescription()


# Page 10
def page_10():
    # st.markdown('<p class="big-font-2">. . . Educatioanl Query Search || Gemini Pro . . .</p>', unsafe_allow_html=True)
    selected_10 = option_menu(menu_title = None,
                        options=["Educational Query"], 
                        icons = ["virus2"], 
                        menu_icon = "cast",
                        default_index = 0,
                        orientation = "horizontal",
                        )
    if selected_10 == "Educational Query":
        Education()
         

def main():
    
    st.sidebar.markdown('<p class="big-font-1">JenD.ai</p>', unsafe_allow_html=True)
    # st.sidebar.info("""Welcome to Google's Gemini 🌟""")
    st.sidebar.image("Image1/17.png")
 
    page = st.sidebar.radio("""**Choose Platform**""",("Let's Talk", "Writer", "Coder", "Email Attender", "Quantumania", "Stock Market", "Web Development", "Prompt & Query", "Educatioanl Query Search"))
    # "File Analyzer",
    if page == "Let's Talk":
        page_1()
    elif page == "Writer":
        page_2()
    # elif page == "File Analyzer":
    #     page_3()
    elif page == "Coder":
        page_4()
    elif page == "Email Attender":
        page_5()
    elif page == "Quantumania":
        page_6()
    elif page == "Stock Market":
        page_7()
    elif page == "Web Development":
        page_8()
    elif page == "Prompt & Query":
        page_9()
    elif page == "Educatioanl Query Search":
        page_10()

    # # 🌟, 🔧
    # with st.sidebar.container(height = 235, border = False):
    #     st.info("""
                    
    #                 ***[:blue[JenDG2.ai]](https://geminijend--phase-1-dpai242.streamlit.app/)***, a Generative AI platform has been created by [:blue[Dipankar Porey]](https://www.linkedin.com/in/dipankar-porey-403320259/), 
    #                 Technology Consultant, Senior at Ernst & Young LLP.
                    
    #                 This application has been built using the Google's Gemini platform, based on the Large Language Models(LLMs).
                    
    #                 🌐Language: English
                    
    #                 🔖Version: Updated with the current version
                    
    #                 📅Date: 10th January, 2023
                    
    #                 """)
    #  Gorq_function(model_name = model_name)

    show_advanced_info_1 = st.sidebar.toggle(":blue[*Show Application Details*]", value = True)
    
    if show_advanced_info_1:
        st.sidebar.info("""

                    **Generative AI application**

                    - **About:** *Multi-application platform*
                    
                    - **Model:** *Gemini backend*
                    
                    - **Language:** *English*
                    
                    - **Release Date:** *December, 2023*
                    
                    """)
        
    show_advanced_info_2 = st.sidebar.toggle(":blue[*Show Developer Details*]", value = False)
    
    if show_advanced_info_2:
        st.sidebar.info("""
                    
                    *This appplication has been created by [:blue[Dipankar Porey]](https://www.linkedin.com/in/dipankar-porey-403320259/), 
                    Technology Consultant, Senior at Ernst & Young LLP.* 
                    
                    """)

       
if __name__ == '__main__':
    main()
