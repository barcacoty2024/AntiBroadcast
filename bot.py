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
    updater = Updater(token=TOKEN_BOT, use_context=True)
    dp = updater.dispatcher

    # Command '/start' untuk memastikan bot aktif
    dp.add_handler(CommandHandler("start", start))

    # Fungsi untuk menangani pesan global atau broadcast
    dp.add_handler(MessageHandler(Filters.TEXT & ~Filters.FORWARD, anti_broadcast_handler))

    # Start the Bot
    updater.start_polling()

    # Keep the program running
    updater.idle()

if __name__ == '__main__':
    main()
