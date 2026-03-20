import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

print("✅ Config loaded!")
print("GROQ:", "OK" if GROQ_API_KEY else "❌ MISSING")
print("OpenRouter:", "OK" if OPENROUTER_API_KEY else "❌ MISSING")
