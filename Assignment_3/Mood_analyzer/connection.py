from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os 
from dotenv import load_dotenv



load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY") # type: ignore

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment value is not set or is empty.")


external_client = AsyncOpenAI(
    api_key=gemini_api_key, # type: ignore
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
       model="gemini-2.0-flash",
       openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True

)