import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏆 Coupe du Monde", callback_data="coupe")],
        [InlineKeyboardButton("📊 Classement FIFA", callback_data="classement")],
        [InlineKeyboardButton("⚽ Matchs du jour", callback_data="matchs")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔥 BG1ER FIFA BOT 🔥\nBienvenue BG ! Choisis :", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Tu as clique sur {query.data} - Bientot les vrais scores BG !\n\nTape /start pour revenir au menu")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot lance")
    app.run_polling()

if __name__ == "__main__":
    main()
