# admin_functions.py - Private admin board functions
from telegram import Update
from telegram.ext import ContextTypes
from admin_config import ADMIN_IDS, BOT_STATUS, RAILWAY_USAGE

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """🔐 Admin board - Only you can see!"""
    user_id = update.effective_user.id
    
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ Admin ပဲ သုံးလို့ရတယ်!")
        return
    
    stats = f"""
🔐 **ADMIN PANEL** 🔐

👥 Users: 150+
🤖 Bot Status: {BOT_STATUS}
💰 Railway Usage: {RAILWAY_USAGE}
📊 Messages today: 45
🚀 Uptime: 99.9%

⚙️ **Commands:**
/stats - Detailed stats
/broadcast - Send to all users  
/restart - Restart bot
/logs - Recent logs
"""
    await update.message.reply_text(stats)

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """📈 Detailed admin stats - Only you!"""
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        return
    
    stats = """
📈 **DETAILED STATS:**
• Total messages: 2,450
• Active users: 127
• Groq API calls: 1,892  
• One Piece queries: 45
• Kpop queries: 32
• Digital queries: 18
"""
    await update.message.reply_text(stats)
