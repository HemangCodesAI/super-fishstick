# Vision2Code

A simple tool to convert screenshots, sketches, and Figma designs into clean, functional code using AI. 



https://github.com/HemangCodesAI/super-fishstick/assets/91689621/d1abe6d9-2315-414f-9449-548f274eb2a2


Supported AI models:

- Gemini-vision-pro
- Gemini-pro

Latest feature update:

- We just added a chat feature that will help you update, improve, and even make corrections to the generated code by chatting with it.
- It is implemented with the Latest Gemini-pro model.

## 🛠 Getting Started

The app has a Streamlit frontend. You will need a Google AI API key.

Install the necessary libraries `pip install -r requirements.txt`

Create a `.env` file and add the `Google_API_KEY` to `.env` with your API key from Google.

Run the command to start the app:
```bash
streamlit run chatapp.py
```


The app will be up and running at localhost. Note that you can develop the application with this setup as the file changes will trigger a rebuild.

## 📚 Examples

**IMDB Page**

| Original                                                                                                                                                        | Replica                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1238" alt="Screenshot 2023-11-20 at 12 54 03 PM" src="https://github.com/HemangCodesAI/super-fishstick/blob/main/examples/image.png"> | <img width="1414" alt="Screenshot 2023-11-20 at 12 59 56 PM" src="https://github.com/HemangCodesAI/super-fishstick/blob/main/examples/imdbexample.jpg"> |

**Portfolio Page**

| Original                                                                                                                                                        | Replica                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1238" alt="Screenshot 2023-11-20 at 12 54 03 PM" src="https://github.com/HemangCodesAI/super-fishstick/blob/main/examples/sample.jpg"> | <img width="1414" alt="Screenshot 2023-11-20 at 12 59 56 PM" src="https://github.com/HemangCodesAI/super-fishstick/blob/main/examples/sample%20example.jpg"> |

