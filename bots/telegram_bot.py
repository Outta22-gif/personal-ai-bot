import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('..')  # Parent directory access for admin modules

from dotenv import load_dotenv
load_dotenv()

from ai_core.groq_client import GroqClient
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

# Admin imports
from admin_functions import admin_panel, admin_stats
from admin_config import ADMIN_IDS

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
client = GroqClient()

async def start(update, context):
    await update.message.reply_text("Yo! Sup")

async def chat(update, context):
    msg = update.message.text
    print(f"👤 User: {msg}")
    await update.message.reply_chat_action("typing")
    
    response = client.chat(msg)
    print(f"🤖 AI: {response[:50]}...")
    await update.message.reply_text(response)

# Admin command handlers
async def admin_panel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await admin_panel(update, context)

async def admin_stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await admin_stats(update, context)

app = Application.builder().token(BOT_TOKEN).build()

# Public handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

# Private admin handlers
app.add_handler(CommandHandler("admin", admin_panel_handler))
app.add_handler(CommandHandler("stats", admin_stats_handler))

print("🚀 Bot starting with admin panel...")
app.run_polling()
