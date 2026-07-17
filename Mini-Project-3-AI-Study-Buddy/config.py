from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

MODEL = "openrouter/auto"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)