from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short joke about programming."
)
print(interaction.output_text)