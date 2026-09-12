import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


ADMIN_USERNAME = "simplicityaccountmanagements"
ADMIN_URL = f"https://t.me/{ADMIN_USERNAME}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📊 View Plans",
                callback_data="plans"
            )
        ],
        [
            InlineKeyboardButton(
                "ℹ️ How It Works",
                callback_data="how"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 Contact Admin",
                callback_data="admin"
            )
        ],
    ]

    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "📊 COPY TRADING PLANS\n\n"
        "Choose an option below to learn more.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    # -------------------------
    # VIEW PLANS
    # -------------------------
    if query.data == "plans":

        keyboard = [
            [
                InlineKeyboardButton(
                    "💵 $300 Plan",
                    callback_data="plan300"
                )
            ],
            [
                InlineKeyboardButton(
                    "💵 $500 Plan",
                    callback_data="plan500"
                )
            ],
            [
                InlineKeyboardButton(
                    "💵 $1,000 Plan",
                    callback_data="plan1000"
                )
            ],
            [
                InlineKeyboardButton(
                    "💵 $5,000 Plan",
                    callback_data="plan5000"
                )
            ],
            [
                InlineKeyboardButton(
                    "📞 Contact Admin",
                    callback_data="admin"
                )
            ],
        ]

        await query.message.reply_text(
            "📊 COPY TRADING PLANS\n\n"

            "💵 $300 PLAN\n"
            "Advertised weekly outcome: $3,000\n\n"

            "💵 $500 PLAN\n"
            "Advertised weekly outcome: $6,000\n\n"

            "💵 $1,000 PLAN\n"
            "Advertised weekly outcome: $9,000\n\n"

            "💵 $5,000 PLAN\n"
            "Advertised weekly outcome: $13,000\n\n"

            "⚠️ IMPORTANT\n"
            "These figures are advertised/projection outcomes "
            "and are NOT guaranteed. Trading involves substantial "
            "risk, including possible loss of capital.\n\n"

            "Please contact the admin for current terms, fees, "
            "requirements and risk information.",

            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    # -------------------------
    # HOW IT WORKS
    # -------------------------
    elif query.data == "how":

        await query.message.reply_text(
            "ℹ️ HOW IT WORKS\n\n"

            "1️⃣ Choose a copy-trading plan.\n\n"
            "2️⃣ Contact the admin for the current requirements "
            "and terms.\n\n"
            "3️⃣ Review all applicable fees, risks and conditions "
            "before proceeding.\n\n"
            "4️⃣ Only proceed after you understand the terms.\n\n"

            "⚠️ Trading profits are not guaranteed. "
            "Capital can be lost.\n\n"

            "📞 For current information, contact the admin.",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "💬 Message Admin",
                        url=ADMIN_URL
                    )
                ]
            ]),
        )

    # -------------------------
    # CONTACT ADMIN
    # -------------------------
    elif query.data == "admin":

        await query.message.reply_text(
            "📞 CONTACT ADMIN\n\n"
            "For plan requirements, current terms, fees "
            "and general information, message the admin directly.\n\n"
            f"@{ADMIN_USERNAME}",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "💬 Message Admin",
                        url=ADMIN_URL
                    )
                ]
            ]),
        )

    # -------------------------
    # $300 PLAN
    # -------------------------
    elif query.data == "plan300":

        await query.message.reply_text(
            "💵 $300 PLAN\n\n"
            "Advertised weekly outcome: $3,000\n\n"

            "⚠️ This is an advertised/projection outcome, "
            "not a guarantee.\n\n"

            "Trading involves risk and capital can be lost.\n\n"

            "📞 Contact the admin for current terms, "
            "fees and requirements.",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "💬 Message Admin",
                        url=ADMIN_URL
                    )
                ]
            ]),
        )

    # -------------------------
    # $500 PLAN
    # -------------------------
    elif query.data == "plan500":

        await query.message.reply_text(
            "💵 $500 PLAN\n\n"
            "Advertised weekly outcome: $6,000\n\n"

            "⚠️ This is an advertised/projection outcome, "
            "not a guarantee.\n\n"

            "Trading involves risk and capital can be lost.\n\n"

            "📞 Contact the admin for current terms, "
            "fees and requirements.",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "💬 Message Admin",
                        url=ADMIN_URL
                    )
                ]
            ]),
        )

    # -------------------------
    # $1,000 PLAN
    # -------------------------
    elif query.data == "plan1000":

        await query.message.reply_text(
            "💵 $1,000 PLAN\n\n"
            "Advertised weekly outcome: $9,000\n\n"

            "⚠️ This is an advertised/projection outcome, "
            "not a guarantee.\n\n"

            "Trading involves risk and capital can be lost.\n\n"

            "📞 Contact the admin for current terms, "
            "fees and requirements.",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "💬 Message Admin",
                        url=ADMIN_URL
                    )
                ]
            ]),
        )

    # -------------------------
    # $5,000 PLAN
    # -------------------------
    elif query.data == "plan5000":

        await query.message.reply_text(
            "💵 $5,000 PLAN\n\n"
            "Advertised weekly outcome: $13,000\n\n"

            "⚠️ This is an advertised/projection outcome, "
            "not a guarantee.\n\n"

            "Trading involves risk and capital can be lost.\n\n"

            "📞 Contact the admin for current terms, "
            "fees and requirements.",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "💬 Message Admin",
                        url=ADMIN_URL
                    )
                ]
            ]),
        )


# -------------------------
# HEALTH CHECK SERVER
# -------------------------

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        pass


def run_web_server():
    port = int(os.environ.get("PORT", 10000))

    server = HTTPServer(
        ("0.0.0.0", port),
        HealthHandler
    )

    server.serve_forever()


# Start health server in background
threading.Thread(
    target=run_web_server,
    daemon=True
).start()


# -------------------------
# TELEGRAM BOT
# -------------------------

token = os.environ.get("BOT_TOKEN")

if not token:
    raise RuntimeError(
        "BOT_TOKEN environment variable is missing."
    )


app = Application.builder().token(token).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CallbackQueryHandler(button_handler)
)


print("Bot is starting...")

app.run_polling()
