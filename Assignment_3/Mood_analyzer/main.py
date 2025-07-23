import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Analyze mood using Gemini
def analyze_mood(feeling: str) -> str:
    prompt = f"""
You are a friendly and emotionally intelligent mood analyzer assistant.

Your task:
1. Analyze the user's emotional state from this input: "{feeling}".
2. Respond with a sentence describing their mood.
3. Briefly share your own matching or empathetic mood.
4. Provide 1-2 short, practical suggestions to improve their mood.

Respond in a kind, encouraging, and helpful tone.
"""
    response = model.generate_content(prompt)
    return response.text

# Chainlit chat app
@cl.on_chat_start
async def start():
    await cl.Message("Hello! How are you feeling today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content
    mood_analysis = analyze_mood(user_input)
    await cl.Message(mood_analysis).send()
