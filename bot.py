from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram import ParseMode
import os

TOKEN_BOT = '6551801424:AAEvoJmcTvxbEoVx6_RdfuokyUBrd7qUFS8'
CHAT_ID_OWNER = 6588255955

def start(update, context):
    update.message.reply_text("Bot is active!")

def anti_broadcast_handler(update, context):
    if update.message and update.message.chat_id == CHAT_ID_OWNER:
        # Pemilik bot dapat melihat pesan di grup
        print(f"Owner Message: {update.message.text}")
    elif update.message and update.message.chat_id != CHAT_ID_OWNER:
        # Non-pemilik bot, blokir pesan global atau broadcast
        update.message.delete()

def main():
    # Port yang diberikan oleh Heroku
    port = int(os.environ.get('PORT', 5000))


    updater = Updater(token=TOKEN_BOT, use_context=True)
    dp = updater.dispatcher

    # Command '/start' untuk memastikan bot aktif
    dp.add_handler(CommandHandler("start", start))

    # Fungsi untuk menangani pesan global atau broadcast
    dp.add_handler(MessageHandler(Filters.text & ~Filters.forwarded, anti_broadcast_handler))

    # Bagian start_webhook
    updater.start_webhook(listen="0.0.0.0", port=int(os.environ.get('PORT', 5000)), url_path=TOKEN_BOT)

    # Bagian setWebhook
    updater.bot.setWebhook(f"https://antip.herokuapp.com/{TOKEN_BOT}")

    # Keep the program running
    updater.idle()

if __name__ == '__main__':
    main()
