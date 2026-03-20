import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import GROQ_API_KEY
from groq import Groq

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
    
    def list_models(self):
        """Get all available models for this account"""
        try:
            models = self.client.models.list()
            return [m.id for m in models.data]
        except:
            return []
    
    def chat(self, message):
        # First, get available models
        available = self.list_models()
        print("📋 Available models:", available[:5], "..." if len(available) > 5 else "")
        
        # Try first 3 available models
        for model in available[:3]:
            try:
                print(f"🔄 Testing: {model}")
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": message}]
                )
                print(f"✅ {model} WORKS!")
                return response.choices[0].message.content
            except Exception as e:
                print(f"❌ {model} failed")
                continue
        
        raise Exception("No working models!")

# Test
if __name__ == "__main__":
    client = GroqClient()
    print("🔍 Discovering your Groq models...")
    result = client.chat("ဟယ်လို! ဘယ် model တွေ ရှိလဲ?")
    print("🎉 AI READY:", result)
