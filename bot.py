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

def handle_messages(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    chat_id = update.message.chat_id

    # Periksa apakah ada perubahan nama atau username
    if user.id in changes_data.get(chat_id, {}):
        context.bot.send_message(chat_id, f"🔄 {user.username} mengganti username menjadi {user.username}!")

        if user.full_name != changes_data[chat_id][user.id].get('full_name'):
            context.bot.send_message(chat_id, f"🔄 {user.username} mengganti nama menjadi {user.full_name}!")

        # Perbarui data perubahan nama dan username
        changes_data[chat_id][user.id] = {'username': user.username, 'full_name': user.full_name}

def main() -> None:
    # Ganti TOKEN_BOT dengan token bot yang Anda dapatkan dari BotFather
    updater = Updater("6551801424:AAEvoJmcTvxbEoVx6_RdfuokyUBrd7qUFS8")

    dp = updater.dispatcher

    # Menangani perintah /start
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^start$'), start))

    # Menangani perubahan member chat (nama dan username)
    dp.add_handler(ChatMemberHandler(handle_chat_member_updated, ChatMemberUpdated))

    # Menangani pesan di grup
    dp.add_handler(MessageHandler(Filters.text & Filters.chat_type.groups, handle_messages))

    # Memulai bot
    updater.start_polling()

    # Menutup bot saat Ctrl+C ditekan
    updater.idle()

if __name__ == '__main__':
    main()
