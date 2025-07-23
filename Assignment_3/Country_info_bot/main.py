import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


def get_country_info_with_gemini(country: str) -> str:
    prompt = f"""
You are a helpful world fact expert.

A user asked about the country: "{country}"

Please return the following information in this format:

1. Capital: ...
2. Official Language(s): ...
3. Population: ...

Only return the info — no extra greetings.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error occurred: {e}"

# Chainlit app
@cl.on_chat_start
async def start():
    await cl.Message("🌍 Hello! Type the name of any country to get its capital, language, and population.").send()

@cl.on_message
async def on_message(message: cl.Message):
    country_name = message.content.strip()
    reply = get_country_info_with_gemini(country_name)
    await cl.Message(reply).send()
