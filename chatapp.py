import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()
API_KEY = os.getenv("Google_API_Key")
genai.configure(api_key=API_KEY)

llm=genai.GenerativeModel('gemini-pro',)
# chat = llm.start_chat(history=[])
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
st.set_page_config( page_icon="📸", layout="wide", initial_sidebar_state="collapsed")

st.title("Vision2Code")
col1, col2 = st.columns(2)
def stream_code(llm,image,input=input):
    res=llm.generate_content([input,image],stream=True,generation_config={"max_output_tokens":4096})
    for chunk in res:
        # generated_code=generated_code+chunk.candidates[0].content.parts[0].text
        yield chunk.candidates[0].content.parts[0].text

def get_gemini_response(question):   
    response=chat.send_message(question,stream=True)
    for chunk in response:
        yield chunk.candidates[0].content.parts[0].text

if "messages" not in st.session_state:
    st.session_state.messages = []

def recusrsive_parser(image):
    vllm=genai.GenerativeModel('gemini-pro-vision')
    print("started")
    try:
        st.session_state["generated_code"]=st.write_stream(stream_code(vllm,image))
        st.session_state["first_phase_complete"]=True 
    except:
        st.write("Network Error!!!")
        regenerate=st.button("Regenerate")
        if regenerate:
            print("restarting")
            recusrsive_parser(image)
# with tab1:
with col1:
    uploaded_file = st.file_uploader("Choose an Image file", accept_multiple_files=False, type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        generate = st.button("Generate!")
        if generate:
            recusrsive_parser(image)
            st.session_state["first_phase_complete"]=True
        else:
            if st.session_state.get("first_phase_complete")!=None:
                st.markdown(st.session_state.get("generated_code"))


chat_command=f'''Yor are a expert web developer and the I have asked you to make me a website as per my design, you have made the webite using Tailwind, HTML and JS
. you have done an excelent job .
here is the code that you gave {st.session_state.get("generated_code")}. 
Now i want you to do some minor updates in this code and help me imporve the code. you will only update the code without adding any comments , you will tell me exactly where in the code i will need to paste the changes.no need to give the final complete updated code.
dont suggest future updates unless asked explicitly.
let me know you are ready for the task by just saying lets go , than i will tell you what updates i want'''
if 'chat_history' not in st.session_state and st.session_state.get("first_phase_complete"):
    chat = llm.start_chat(history=[])
    res=chat.send_message(chat_command)
    st.session_state['chat_history'] = chat.history
chat=llm.start_chat(history=st.session_state.get("chat_history"))


with col2:
    if st.session_state.get("first_phase_complete"):
        # st.write("cahtbot mode")
        # chat.history
        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                response=st.write_stream(get_gemini_response(prompt))
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state['chat_history']=chat.history
        for message in st.session_state.messages[:-1:-1]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    else :
        st.image('examples/bot.jpg')
        "## Upload you design or screenshot to begin code generation."
        