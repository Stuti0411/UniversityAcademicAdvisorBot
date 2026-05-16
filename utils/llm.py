
from groq import Groq
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError(f"GROQ_API_KEY not found. Ensure {env_path} exists and contains the key.")

client = Groq(
    api_key=api_key
)

def get_llm_response(prompt):
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [{"role":"user",
                     "content": prompt}]
    )
    return response.choices[0].message.content