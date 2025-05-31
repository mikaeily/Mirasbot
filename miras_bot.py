
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Load Telegram Bot Token from Environment Variables
TOKEN = os.environ.get("TOKEN")

# Basic Logging Setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 MIRAS AI: فعال‌سازی شد.")

# Echo Handler for all text messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = f"🎯 میکائیل ژن پاسخ میده: «{user_input}»\n⌛️ [در حال تحلیل عمیق...]"
    await update.message.reply_text(response)

# Main Entry Point
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()
