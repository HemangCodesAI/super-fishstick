import chainlit as cl
# import openai
import os
import google.generativeai as genai
# from langchain import PromptTemplate, LLMChain
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage
import PIL.Image
from dotenv import load_dotenv
load_dotenv()

def remove_subfolders(folder_path):
    # Iterate over all items in the directory
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        print(item_path)
        print("1")
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Recursively remove subfolders
            remove_subfolders(item_path)
            # Remove the empty directory
            os.rmdir(item_path)
        elif os.path.isfile(item_path):
            os.remove(item_path)

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

def process_image():
    try:
        folder_path=os.path.join(".files",os.listdir('.files\\')[0])
        for file in os.listdir(folder_path):
            print(file)
            img_path=os.path.join(folder_path,file)

    except:
        print("no image")
    # img=[]
    return img_path

# def get_code(img,llm,input=input):
    # res=llm.generate_content([input,img],stream=True,generation_config={"max_output_tokens":4096})
    # return res.content

# async_get_code=cl.make_async(get)
# @cl.on_chat_start
# def main():
#     load_dotenv()
#     genai.configure(api_key=os.getenv("google_ai_key"))
#     llm=genai.GenerativeModel('gemini-pro-vision')
#     cl.user_session.set("llm",llm)

@cl.on_chat_start
async def start():
    
    load_dotenv()
    genai.configure(api_key=os.getenv("google_ai_key"))
    llm=genai.GenerativeModel('gemini-pro-vision')
    cl.user_session.set("llm",llm)
    files = None

    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a text file to begin!", accept=[""]
        ).send()

    # img_file = files[0]
    img=PIL.Image.open(process_image())

    # with open(text_file.path, "r", encoding="utf-8") as f:
    #     text = f.read()

    # Let the user know that the system is ready
    await cl.Message(
        content=f"`phot"
    ).send()


@cl.on_message
async def main(message : cl.Message):
    llm=cl.user_session.get("llm")
    img=PIL.Image.open(process_image())
    print("started")
    res=llm.generate_content([input,img],stream=True,generation_config={"max_output_tokens":4096})
    # res="abra ca dabra"
    # # for chunk in res:
    # #     await cl.Message(content=chunk.candidates[0].content.parts[0].text).send()
    cl.Message(content=res.content).send()
    # await cl.Message(content=res).send()

@cl.on_chat_end
def end():
    print("goodbye", cl.user_session.get("id"))
    remove_subfolders(".files\\")