from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# Dictionary untuk menyimpan data perubahan nama dan username
changes_data = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Selamat datang di Bot Pemantau Perubahan Nama dan Username!")

def handle_message(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id

    # Periksa apakah ada perubahan nama atau username
    if user.username != changes_data.get(chat_id, {}).get(user.id, {}).get('username'):
        update.message.reply_text(f"🔄 {user.username} mengganti username menjadi {user.username}!")

    if user.full_name != changes_data.get(chat_id, {}).get(user.id, {}).get('full_name'):
        update.message.reply_text(f"🔄 {user.username} mengganti nama menjadi {user.full_name}!")

    # Perbarui data perubahan nama dan username
    if chat_id not in changes_data:
        changes_data[chat_id] = {}
    changes_data[chat_id][user.id] = {'username': user.username, 'full_name': user.full_name}

def main() -> None:
    # Ganti TOKEN_BOT dengan token bot yang Anda dapatkan dari BotFather
    updater = Updater("6551801424:AAEvoJmcTvxbEoVx6_RdfuokyUBrd7qUFS8")

    dp = updater.dispatcher

    # Menangani perintah /start
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^start$'), start))

    # Menangani setiap pesan di grup
    dp.add_handler(MessageHandler(Filters.chat_type.groups, handle_message))

    # Memulai bot
    updater.start_polling()

    # Menutup bot saat Ctrl+C ditekan
    updater.idle()

if __name__ == '__main__':
    main()
