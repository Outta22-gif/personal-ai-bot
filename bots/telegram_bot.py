import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

from ai_core.groq_client import GroqClient
from telegram.ext import Application, CommandHandler, MessageHandler, filters

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
client = GroqClient()

async def start(update, context):
    await update.message.reply_text("🤖 Groq AI Bot ready!\nမေးချင်တာ မေးပါ!")

async def chat(update, context):
    msg = update.message.text
    print(f"👤 User: {msg}")
    await update.message.reply_chat_action("typing")
    
    response = client.chat(msg)
    print(f"🤖 AI: {response[:50]}...")
    await update.message.reply_text(response)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("🚀 Bot starting...")
app.run_polling()
