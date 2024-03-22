from telegram import Update, ChatMemberUpdated
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, ChatMemberHandler, CommandHandler

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

        # Simpan riwayat perubahan nama
        save_name_change(update.message.chat_id, new_chat_member.id, old_chat_member.full_name)

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
        save_name_change(chat_id, user.id, user.full_name)

def list_previous_names(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    previous_names = get_previous_names(chat_id, user_id)

    if previous_names:
        message = f"Daftar nama sebelumnya untuk pengguna ini:\n{', '.join(previous_names)}"
    else:
        message = "Pengguna ini tidak memiliki daftar nama sebelumnya."

    context.bot.send_message(chat_id, message)

def save_name_change(chat_id, user_id, new_full_name):
    if chat_id not in changes_data:
        changes_data[chat_id] = {}
    if user_id not in changes_data[chat_id]:
        changes_data[chat_id][user_id] = {'username': '', 'full_name': []}
    changes_data[chat_id][user_id]['full_name'].append(new_full_name)

def get_previous_names(chat_id, user_id):
    if chat_id in changes_data and user_id in changes_data[chat_id]:
        return changes_data[chat_id][user_id]['full_name']
    return []

def simple_response(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, "Ini adalah respons sederhana.")

def main() -> None:
    # Ganti TOKEN_BOT dengan token bot yang Anda dapatkan dari BotFather
    updater = Updater("7134404818:AAED5iwrScJXVtehRa8QogJTZ2YXRqoK1e8")

    dp = updater.dispatcher

    # Menangani perintah /start
    dp.add_handler(CommandHandler('start', start))

    # Menangani perubahan member chat (nama dan username)
    dp.add_handler(ChatMemberHandler(handle_chat_member_updated, ChatMemberUpdated))

    # Menangani pesan di grup
    dp.add_handler(MessageHandler(Filters.text & Filters.chat_type.groups, handle_messages))

    # Menangani perintah /sa
    dp.add_handler(CommandHandler('sa', list_previous_names))

    # Menangani perintah /test
    dp.add_handler(CommandHandler('test', simple_response))

    # Memulai bot
    updater.start_polling()

    # Menutup bot saat Ctrl+C ditekan
    updater.idle()

if __name__ == '__main__':
    main()
