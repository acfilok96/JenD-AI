import time
import streamlit as st
from excuses import Excuses
from prompts import PromptCls
from geminiKey import GeminiKey
import google.generativeai as geminiai
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import PIL.Image

# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename) # , color_mode = "grayscale", target_size=(1080, 1080))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 1 channel
    # img = img.reshape(1, 28, 28, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img

def ImageDescription():
    
    geminiai.configure(api_key = str(GeminiKey()))  # "AIzaSyAde1168Yh8ORh8GS-jFMWMDNg7h5RbiHw"
    
    ################################################
    
    model = geminiai.GenerativeModel("gemini-pro-vision")
    
    ################################################
    container_1 = st.container(height = 350, border = False)

    with container_1:
        st.title("`Image Description`")
        st.info("Please upload the image and put your query here. Thank you!")
        
        ################################################
        col1, col2 = st.columns(2)
            
        query = ""
        with col1:
            query = st.text_input(":blue[Query]", placeholder='Enter your query here . . .') #  "Enter your query here . . ." # , key=placeholder
        
        with col2:
            images = st.file_uploader(":blue[Upload image]", type=["png","jpg","jpeg"], accept_multiple_files=False)
        
        
    ################################################
        if st.button("Get your response!"):
                 
            if query:
                if images:
    
                    
                    # To See details
                    # file_details = {"filename":images.name, "filetype":images.type, "filesize(Byte)":images.size}
                    # st.write(file_details)
                    st.markdown(f"Image Name: {images.name}")
                    st.markdown(f"Image Type: {images.type}")
                    st.markdown(f"Image Size[In Byte]: {images.size}")
    
                    img = load_image(images)
                    # To View Uploaded Image
                    st.image(img)
                            
                    with st.chat_message("user"):
                        st.markdown(query)
                
                    with st.chat_message("assistant"):
                        message_placeholder = st.empty()
                        with st.spinner("Processing your response..."):
                            try: 
                                full_response = ""
                                query = PromptCls.ImagePromptClash(query)
                                imgs = PIL.Image.open(images)
                                response = model.generate_content([query, imgs], generation_config={"temperature": 0.2})
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
                            st.success("Done!")
