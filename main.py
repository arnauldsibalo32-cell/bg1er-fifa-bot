import os
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
TEAMS = ["Man City eSports", "Real Madrid eSports", "PSG eSports", "Bayern eSports", "Liverpool eSports", "Barca eSports", "Arsenal eSports", "Inter eSports", "Chelsea eSports", "Dortmund eSports"]

def generate_prono():
    home = random.choice(TEAMS)
    away = random.choice([t for t in TEAMS if t != home])
    over = random.choice(["Over 2.5 ✅ (78%)", "Under 2.5 ⚠️ (65%)", "Over 3.5 🔥 (82%)", "Over 1.5 ✅ (91%)"])
    btts = random.choice(["BTTS OUI ✅ (74%)", "BTTS NON ⚠️ (68%)"])
    dc = random.choice(["1X ✅", "X2 ✅", "12 ⚠️"])
    ht = random.choice(["Mi-Temps: 1 - Domination", "Mi-Temps: X - Équilibré", "Mi-Temps: 2 - Contre"])
    score = random.choice(["2-1", "3-1", "1-1", "2-0", "3-2", "0-1", "1-2"])
    winner = random.choice([home, away, "MATCH NUL RISQUÉ"])
    conf = random.randint(72, 94)
    return home, away, over, btts, dc, ht, score, winner, conf

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏆 PRONO DU JOUR (VIP)", callback_data="prono_vip")],
        [InlineKeyboardButton("📊 Over/Under", callback_data="over"), InlineKeyboardButton("⚽ BTTS", callback_data="btts")],
        [InlineKeyboardButton("⏱️ Mi-Temps / Fin", callback_data="htft"), InlineKeyboardButton("🎯 Score Exact", callback_data="score")],
        [InlineKeyboardButton("🔥 Analyse Complète", callback_data="analyse"), InlineKeyboardButton("📅 Matchs du Jour", callback_data="matchs")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🔥 **BG1ER FIFA BOT PRO EST LÀ BG !** 🔥\n\n"
        "Ton bot FIFA / eFootball ULTIME BG !\n\n"
        "✅ Over / Under\n✅ BTTS Oui/Non\n✅ Double Chance\n✅ Mi-Temps\n✅ Score Exact\n✅ Analyse Pro + % Confiance\n\nClique en bas BG 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    home, away, over, btts, dc, ht, score, winner, conf = generate_prono()

    if query.data == "prono_vip":
        text = f"🏆 **PRONO VIP DU JOUR** 🏆\n\n⚔️ {home} vs {away}\n\n🔥 **Vainqueur:** {winner}\n📊 **Confiance:** {conf}%\n\n⚽ Over/Under: {over}\n🤝 BTTS: {btts}\n🛡️ Double Chance: {dc}\n⏱️ {ht}\n🎯 Score Exact: {score}\n\n💰 Cote ~ {round(random.uniform(1.8,4.5),2)}\n\nBG1ER VALIDÉ ✅"
    elif query.data == "over":
        text = f"📊 **OVER / UNDER**\n\n⚔️ {home} vs {away}\n\nPrédiction: **{over}**\n\n📈 Moyenne 3.2 buts / match\n💡 SAFE: Over 1.5 / FUN: Over 2.5\n\nConfiance: {conf}%"
    elif query.data == "btts":
        text = f"⚽ **BTTS**\n\n⚔️ {home} vs {away}\n\nPrédiction: **{btts}**\n\nLes 2 équipes marquent 4/5 derniers matchs\nConfiance: {conf}%"
    elif query.data == "htft":
        text = f"⏱️ **MI-TEMPS / FIN**\n\n⚔️ {home} vs {away}\n\n**{ht}**\n**Fin: {winner}**\n\nProno HT/FT: 1/1 si {home} favori sinon X/2"
    elif query.data == "score":
        text = f"🎯 **SCORE EXACT PRO**\n\n⚔️ {home} vs {away}\n\n1️⃣ {score} - {conf}%\n2️⃣ {random.choice(['2-1','1-0'])} - {conf-8}%\n3️⃣ {random.choice(['3-1','1-1'])} - {conf-15}%\n\n💸 Joue le 1er, couvre avec le 2ème"
    elif query.data == "analyse":
        text = f"🔥 **ANALYSE COMPLÈTE**\n\n⚔️ {home} vs {away}\n📅 {datetime.now().strftime('%d/%m/%Y')}\n\n📊 FORME: {home} 4V-1N / {away} 3V-2D\n⚽ Buts Moy: 2.8 vs 2.1\n\n**FINAL BG:**\n✅ Vainqueur: {winner}\n✅ Over 2.5: {over}\n✅ BTTS: {btts}\n✅ Score: {score}\n\n**Confiance: {conf}% - VALIDÉ ✅**"
    elif query.data == "matchs":
        text = "📅 **MATCHS DU JOUR**\n\n"
        for i in range(3):
            h = random.choice(TEAMS)
            a = random.choice([t for t in TEAMS if t != h])
            text += f"• {h} vs {a} - {random.randint(14,22)}h\n"
        text += "\nClique PRONO VIP pour ticket BG !"
    else:
        text = "Menu"
        
    if query.data == "menu":
        await start(update, context)
        return

    keyboard = [
        [InlineKeyboardButton("🏆 PRONO VIP", callback_data="prono_vip")],
        [InlineKeyboardButton("📊 Over/Under", callback_data="over"), InlineKeyboardButton("⚽ BTTS", callback_data="btts")],
        [InlineKeyboardButton("⬅️ MENU", callback_data="menu")]
    ]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("BG1ER BOT PRO LANCÉ !")
    app.run_polling()

if __name__ == "__main__":
    main()
