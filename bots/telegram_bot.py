import sys
import os
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CommandHandler
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
🚀 **Welcome to FutureBot!**

Yo! Sup 👋 Choose a command:

**Quick Access:**
/start - Start the FutureBot
/travel - Thailand travel updates  
/onepiece - One Piece information and update news
/kpop - K-Pop artists and news
/digital - Digital marketing tips
/cannabis - Thailand Cannabis news update
/broadcast - Send message to all users (Admin)
/feedback - Send feedback to admin
    """
    
    # BotFather commands နဲ့ match ဖြစ်အောင်
    keyboard = [
        [types.KeyboardButton("/travel"), types.KeyboardButton("/cannabis")],
        [types.KeyboardButton("/kpop"), types.KeyboardButton("/onepiece")],
        [types.KeyboardButton("/digital"), types.KeyboardButton("/feedback")]
    ]
    reply_markup = types.ReplyKeyboardMarkup(
        keyboard, 
        resize_keyboard=True, 
        one_time_keyboard=False
    )
    
    await update.message.reply_text(
        welcome_text, 
        reply_markup=reply_markup, 
        parse_mode='Markdown'
    )

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

# K-Pop handler
async def kpop_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎤 **K-Pop News:**\n• BTS comeback Mar 22\n• NCT Wish new album soon\n• aespa US tour started")

# One Piece handler  
async def onepiece_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏴‍☠️ **One Piece:**\n• Ch 1174: Loki dragon form!\n• Luffy Gear 5 active\n• Ch 1175 next week")

# Digital handler
async def digital_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💻 **Digital Tips:**\n• AI content = 10x faster\n• Telegram bots = 24/7 service\n• Myanmar: Video > Text 80%")

# Thailand Cannabis handler
async def cannabis_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🌿 **Thailand Cannabis Farms Latest:**

• **Krabi raid (Jan 2026):** Foreign-funded farm shut down
• DBD found Thai nominees hiding foreign ownership  
• 18,000+ shops face closure after 2025 medical-only law
• Online sales + delivery banned

Recreational use ending fast!
    """, parse_mode='Markdown')

# Thailand Travel handler  
async def travel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
✈️ **Thailand Travel 2026 Updates:**

• **New 6-month MEV visa:** Stay up to 270 days
• Visa-free → 60 → 30 days? (TBD)
• Tourist tax: 300 THB  
• Departure tax update coming
• Immigration warnings issued

Plan ahead!
    """, parse_mode='Markdown')

# Add ALL handlers (မင်းရဲ့ existing handlers အောက်မှာ ထည့်ပါ)
app.add_handler(CommandHandler("kpop", kpop_handler))
app.add_handler(CommandHandler("onepiece", onepiece_handler))
app.add_handler(CommandHandler("digital", digital_handler))
app.add_handler(CommandHandler("cannabis", cannabis_handler))
app.add_handler(CommandHandler("travel", travel_handler))

print("🚀 Bot starting with admin panel...")
app.run_polling(drop_pending_updates=True)

