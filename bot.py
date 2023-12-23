from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram.ext.filters import Filters
from telegram import ParseMode

# ...

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

    updater.start_polling()
    updater.idle()

# ...
