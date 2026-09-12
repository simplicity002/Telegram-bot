from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Please choose an option:\n"
        "💰 Make Payment\n"
        "📞 Contact Admin"
    )

app = Application.builder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
