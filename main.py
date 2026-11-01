import os
import random
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")
TEAMS = ["Man City eSports", "Real Madrid eSports", "PSG eSports", "Barca eSports", "Liverpool", "Arsenal", "Chelsea", "Bayern"]

def generate_prono():
    home = random.choice(TEAMS)
    away = random.choice([t for t in TEAMS if t != home])
    over = random.choice(["Over 2.5", "Under 2.5"])
    btts = random.choice(["BTTS OUI", "BTTS NON"])
    dc = random.choice(["1X", "X2", "12"])
    ht = random.choice(["Mi-Temps: 1", "Mi-Temps: X", "Mi-Temps: 2"])
    score = random.choice(["2-1", "3-1", "1-1", "2-0"])
    winner = random.choice([home, away])
    conf = random.randint(72, 94)
    return home, away, over, btts, dc, ht, score, winner, conf

def start(update: Update, context: CallbackContext):
    keyboard = [['🏆 Prono du Jour', '📊 Stats'], ['⚽ Matchs', '💰 VIP']]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("🔥 BIENVENUE BG ! BOT FIFA EN LIGNE ! 🔥\n\nClique 👇", reply_markup=markup)

def handle_msg(update: Update, context: CallbackContext):
    text = update.message.text
    if "Prono" in text:
        home, away, over, btts, dc, ht, score, winner, conf = generate_prono()
        msg = f"🏆 PRONO FIFA eSports\n\n⚽ {home} vs {away}\n\n✅ {over}\n✅ {btts}\n✅ Double Chance: {dc}\n✅ {ht}\n✅ Score exact: {score}\n\n🔥 Vainqueur: {winner}\n📈 Confiance: {conf}%\n\n💰 Cote: 3.45"
        update.message.reply_text(msg)
    elif "Stats" in text:
        update.message.reply_text("📊 STATS BG : 78% de réussite ! 23/30 gagnés ce mois !")
    elif "Matchs" in text:
        update.message.reply_text("⚽ MATCHS DU JOUR:\n- Man City vs PSG (18h)\n- Real vs Barca (20h)")
    elif "VIP" in text:
        update.message.reply_text("💰 VIP BG1ER : Gagne 10x plus ! Contact @bg1er")
    else:
        update.message.reply_text("Tape /start bg !")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_msg))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
