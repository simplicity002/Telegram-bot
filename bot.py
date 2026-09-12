import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Please choose an option:\n"
        "💰 Make Payment\n"
        "📞 Contact Admin"
    )

token = os.getenv("BOT_TOKEN")

app = Application.builder().token(token).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
