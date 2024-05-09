import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from PIL import Image
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("google_ai_key")
genai.configure(api_key=API_KEY)
input ='''You have perfect vision and pay great attention to detail which makes you an expert at building single page apps using Tailwind, HTML and JS.
    You take screenshots of a reference web page from the user, and then build single page apps 
    using Tailwind, HTML and JS.

    - Make sure the app looks exactly like the screenshot.
    - Do not leave out smaller UI elements. Make sure to include every single thing in the screenshot.
    - Pay close attention to background color, text color, font size, font family, 
    padding, margin, border, etc. Match the colors and sizes exactly.
    - In particular, pay attention to background color and overall color scheme.
    - Use the exact text from the screenshot.
    - Do not add comments in the code such as "<!-- Add other navigation links as needed -->" and "<!-- ... other news items ... -->" in place of writing the full code. WRITE THE FULL CODE.
    - Make sure to always get the layout right (if things are arranged in a row in the screenshot, they should be in a row in the app as well)
    - Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
    - For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.

    In terms of libraries,

    - Use this script to include Tailwind: <script src="https://cdn.tailwindcss.com"></script>
    - You can use Google Fonts
    - Font Awesome for icons: <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"></link>

    Return only the full code in <html></html> tags.
    '''

def stream_code(llm,image,input=input):
    res=llm.generate_content([input,image],stream=True,generation_config={"max_output_tokens":4096})
    for chunk in res:
        yield chunk.candidates[0].content.parts[0].text
    

st.set_page_config( page_icon="📸", layout="centered", initial_sidebar_state="collapsed")
st.header("Google AI Studio + Gemini Pro")
uploaded_file = st.file_uploader("Choose an Image file", accept_multiple_files=False, type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    bytes_data = uploaded_file.getvalue()
    generate = st.button("Generate!")
    if generate:
        llm=genai.GenerativeModel('gemini-pro-vision')
        print("started")
        # res=llm.generate_content([input,image],stream=True,generation_config={"max_output_tokens":4096})
        st.write_stream(stream_code(llm,image))
        # st.write(res.text)