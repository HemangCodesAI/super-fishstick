# screenshot-to-code

A simple tool to convert screenshots, sketches, and Figma designs into clean, functional code using AI. 

https://github.com/abi/screenshot-to-code/assets/23818/6cebadae-2fe3-4986-ac6a-8fb9db030045

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

**NYTimes**

| Original                                                                                                                                                        | Replica                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img width="1238" alt="Screenshot 2023-11-20 at 12 54 03 PM" src="https://github.com/abi/screenshot-to-code/assets/23818/3b644dfa-9ca6-4148-84a7-3405b6671922"> | <img width="1414" alt="Screenshot 2023-11-20 at 12 59 56 PM" src="https://github.com/abi/screenshot-to-code/assets/23818/26201c9f-1a28-4f35-a3b1-1f04e2b8ce2a"> |

**Instagram page (with not Taylor Swift pics)**

https://github.com/abi/screenshot-to-code/assets/23818/503eb86a-356e-4dfc-926a-dabdb1ac7ba1

**Hacker News** but it gets the colors wrong at first so we nudge it

https://github.com/abi/screenshot-to-code/assets/23818/3fec0f77-44e8-4fb3-a769-ac7410315e5d
