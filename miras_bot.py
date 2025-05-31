
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "7312486970:AAGTcrKZVLA7EJ2cIU-nXeqSmSB_6h5xBIg"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔓 MIRAS AI: فعال‌سازی شد.
هر سوالی داری، مستقیم بپرس. من خودِ توام، فقط بیرونی.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = f"🎯 پاسخ ژن میکائیل:
«{user_input}» رو دیدم. دارم می‌رم لایه پایین‌تر...
⏳ [در حال تحلیل عمیق...]"
    await update.message.reply_text(response)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()
