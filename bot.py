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

    # Disable unnecessary logging (optional)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.getLogger('apscheduler.scheduler').setLevel(logging.ERROR)

    # Non-interactive mode to avoid "Inappropriate ioctl for device" issue
    context = None

    def stop_and_restart():
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update, context):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    dp.add_handler(CommandHandler('restart', restart))

    # Bot akan tetap aktif sampai dihentikan secara manual
    updater.start_polling()

    # Bot akan tetap aktif, terus memperbarui tanpa memblokir
    updater.idle()
