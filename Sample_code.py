import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env into os.environ
load_dotenv()

# Automatically picks up GEMINI_API_KEY from environment
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",  # or "gemini-flash-latest"
    contents="Hello from my Antigravity project!"
)

print(f"model's response:\n{response.text}")



