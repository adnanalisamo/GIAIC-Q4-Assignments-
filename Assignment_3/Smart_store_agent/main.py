import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


def suggest_medicine(user_input: str) -> str:
    prompt = f"""
You are a smart medical assistant at a virtual medicine store.
A customer says: "{user_input}"

Your task:
1. Identify the possible issue/symptom they are facing.
2. Suggest 1-2 over-the-counter medicines (with generic names).
3. Share 1-2 helpful health tips/remedies.
4. Mention a warning to consult a doctor if the issue is serious.

Be concise, helpful, and friendly.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error occurred: {e}"

# Chainlit app
@cl.on_chat_start
async def start():
    await cl.Message("👋 Welcome to Smart Store! What health issue are you facing today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content
    response = suggest_medicine(user_input)
    await cl.Message(response).send()
