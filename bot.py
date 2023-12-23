# bot.py
from telegram.ext import Updater, MessageHandler, Filters

# Ganti TOKEN_BOT dengan token yang diberikan oleh BotFather
TOKEN_BOT = '6551801424:AAEvoJmcTvxbEoVx6_RdfuokyUBrd7qUFS8'

# Ganti CHAT_ID dengan ID grup Anda
CHAT_ID = -1002044156039

def anti_broadcast_handler(update, context):
    if update.message and update.message.chat_id == CHAT_ID:
        update.message.delete()

def main():
    updater = Updater(token=TOKEN_BOT, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.TEXT & ~Filters.FORWARD, anti_broadcast_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
