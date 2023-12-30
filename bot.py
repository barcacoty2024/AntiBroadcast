from telegram import Update, ChatMemberUpdated
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, ChatMemberHandler

# Dictionary untuk menyimpan data perubahan nama dan username
changes_data = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Selamat datang di Bot Pemantau Perubahan Nama dan Username!")

def handle_chat_member_updated(update: Update, context: CallbackContext) -> None:
    new_chat_member = update.message.new_chat_members[0] if update.message.new_chat_members else None
    old_chat_member = update.message.old_chat_members[0] if update.message.old_chat_members else None

    # Periksa apakah ada perubahan nama atau username
    if new_chat_member and old_chat_member and new_chat_member.username != old_chat_member.username:
        context.bot.send_message(update.message.chat_id, f"🔄 {new_chat_member.username} mengganti username menjadi {new_chat_member.username}!")

    if new_chat_member and old_chat_member and new_chat_member.full_name != old_chat_member.full_name:
        context.bot.send_message(update.message.chat_id, f"🔄 {new_chat_member.username} mengganti nama menjadi {new_chat_member.full_name}!")

def main() -> None:
    # Ganti TOKEN_BOT dengan token bot yang Anda dapatkan dari BotFather
    updater = Updater("6551801424:AAEvoJmcTvxbEoVx6_RdfuokyUBrd7qUFS8")

    dp = updater.dispatcher

    # Menangani perintah /start
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^start$'), start))

    # Menangani perubahan member chat (nama dan username)
    dp.add_handler(ChatMemberHandler(handle_chat_member_updated, ChatMemberUpdated))

    # Memulai bot
    updater.start_polling()

    # Menutup bot saat Ctrl+C ditekan
    updater.idle()

if __name__ == '__main__':
    main()
