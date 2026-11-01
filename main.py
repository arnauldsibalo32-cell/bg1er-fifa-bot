import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
TEAMS = ["Man City eSports", "Real Madrid eSports", "PSG eSports", "Barca eSports", "Liverpool", "Arsenal", "Chelsea", "Bayern"]

def generate_prono():
    home = random.choice(TEAMS)
    away = random.choice([t for t in TEAMS if t != home])
    over = random.choice(["Over 2.5", "Under 2.5"])
    btts = random.choice(["BTTS OUI", "BTTS NON"])
    dc = random.choice(["1X", "X2", "12"])
    score = random.choice(["2-1", "3-1", "1-1", "2-0"])
    winner = random.choice([home, away])
    conf = random.randint(72, 94)
    return home, away, over, btts, dc, score, winner, conf

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['🏆 Prono du Jour', '📊 Stats'], ['⚽ Matchs', '💰 VIP']]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🔥 BIENVENUE BG ! BOT FIFA EN LIGNE ! 🔥\n\nClique 👇", reply_markup=markup)

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "Prono" in text:
        home, away, over, btts, dc, score, winner, conf = generate_prono()
        msg = f"🏆 PRONO FIFA eSports\n\n⚽ {home} vs {away}\n\n✅ {over}\n✅ {btts}\n✅ Double Chance: {dc}\n✅ Score: {score}\n\n🔥 Vainqueur: {winner}\n📈 Confiance: {conf}%\n\n💰 Cote: 3.45"
        await update.message.reply_text(msg)
    elif "Stats" in text:
        await update.message.reply_text("📊 STATS BG : 78% de réussite ! 23/30 gagnés ce mois !")
    elif "Matchs" in text:
        await update.message.reply_text("⚽ MATCHS:\n- Man City vs PSG (18h)\n- Real vs Barca (20h)")
    elif "VIP" in text:
        await update.message.reply_text("💰 VIP BG1ER : Contact @bg1er")
    else:
        await update.message.reply_text("Tape /start bg !")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))
    app.run_polling()

if __name__ == '__main__':
    main()
