import os
print("🔍 Step 1: Raw environment check")
print("Current folder:", os.getcwd())

from dotenv import load_dotenv
print("🔍 Step 2: Loading .env file...")
result = load_dotenv(verbose=True)
print("Load result:", result)

groq_key = os.getenv("GROQ_API_KEY")
openrouter_key = os.getenv("OPENROUTER_API_KEY")

print("🔍 Step 3: Keys check")
print("GROQ key exists:", bool(groq_key))
print("GROQ length:", len(groq_key) if groq_key else 0)
print("OpenRouter exists:", bool(openrouter_key))
print("OpenRouter length:", len(openrouter_key) if openrouter_key else 0)

print("\n🔍 Step 4: .env file content:")
try:
    with open('.env', 'r') as f:
        content = f.read()
        print("File content:", repr(content))
except:
    print(".env file not found!")
