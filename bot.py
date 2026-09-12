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
        [InlineKeyboardButton("📊 View Plans", callback_data="plans")],
        [InlineKeyboardButton("ℹ️ How It Works", callback_data="how")],
        [InlineKeyboardButton("📞 Contact Admin", callback_data="admin")],
    ]

    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "📊 COPY TRADING PLANS\n\n"
        "Choose an option below to learn more.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "plans":
        keyboard = [
            [InlineKeyboardButton("💵 $300 Plan", callback_data="plan300")],
            [InlineKeyboardButton("💵 $500 Plan", callback_data="plan500")],
            [InlineKeyboardButton("💵 $1,000 Plan", callback_data="plan1000")],
            [InlineKeyboardButton("💵 $5,000 Plan", callback_data="plan5000")],
            [InlineKeyboardButton("📞 Contact Admin", callback_data="admin")],
        ]

        await query.message.reply_text(
            "📊 COPY TRADING PLANS\n\n"
            "💵 $300 Plan\n"
            "Advertised weekly outcome: $3,000\n\n"
            "💵 $500 Plan\n"
            "Advertised weekly outcome: $6,000\n\n"
            "💵 $1,000 Plan\n"
            "Advertised weekly outcome: $9,000\n\n"
            "💵 $5,000 Plan\n"
            "Advertised weekly outcome: $13,000\n\n"
            "⚠️ These figures are advertised/projection outcomes "
            "and are NOT guaranteed. Trading involves substantial risk.",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "how":
        await query.message.reply_text(
            "ℹ️ HOW IT WORKS\n\n"
            "1️⃣ Choose a copy-trading plan.\n"
            "2️⃣ Contact the admin for current terms and instructions.\n"
            "3️⃣ Review the risks and applicable fees before proceeding.\n"
            "4️⃣ Only proceed after you understand the terms.\n\n"
            "⚠️ Trading profits are not guaranteed and capital can be lost."
        )

    elif query.data == "admin":
        await query.message.reply_text(
            "📞 CONTACT ADMIN\n\n"
            "For more information, contact:\n"
            "@simplicityaccountmanagements"
        )

    elif query.data == "plan300":
        await query.message.reply_text(
            "💵 $300 PLAN\n\n"
            "Advertised weekly outcome: $3,000\n\n"
            "⚠️ This is an advertised/projection outcome, not a guarantee.\n"
            "Please contact the admin for current terms, fees and risk information."
        )

    elif query.data == "plan500":
        await query.message.reply_text(
            "💵 $500 PLAN\n\n"
            "Advertised weekly outcome: $6,000\n\n"
            "⚠️ This is an advertised/projection outcome, not a guarantee.\n"
            "Please contact the admin for current terms, fees and risk information."
        )

    elif query.data == "plan1000":
        await query.message.reply_text(
            "💵 $1,000 PLAN\n\n"
            "Advertised weekly outcome: $9,000\n\n"
            "⚠️ This is an advertised/projection outcome, not a guarantee.\n"
            "Please contact the admin for current terms, fees and risk information."
        )

    elif query.data == "plan5000":
        await query.message.reply_text(
            "💵 $5,000 PLAN\n\n"
            "Advertised weekly outcome: $13,000\n\n"
            "⚠️ This is an advertised/projection outcome, not a guarantee.\n"
            "Please contact the admin for current terms, fees and risk information."
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


token = os.environ.get("BOT_TOKEN")

app = Application.builder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
