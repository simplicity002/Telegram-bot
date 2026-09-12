import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Make Payment", callback_data="payment")],
        [InlineKeyboardButton("📞 Contact Admin", url="https://t.me/simplicityaccountmanagements")],
    ]

    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Please choose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "payment":
        await query.message.reply_text(
            "💰 PAYMENT INFORMATION\n\n"
            "Network: BEP20 (BSC)\n"
            "Currency: USDT\n\n"
            "Send USDT to this wallet address:\n\n"
            "0x5adc94bf41bdab0d9f9bb715ae9e6a4e80803462\n\n"
            "⚠️ Make sure you select the BEP20 network."
        )


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        pass


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


threading.Thread(target=run_web_server, daemon=True).start()

token = os.getenv("BOT_TOKEN")

app = Application.builder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
