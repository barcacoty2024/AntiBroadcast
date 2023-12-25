import openai
from telegram.ext import Updater, MessageHandler, Filters

openai.api_key = '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'

def respond_to_message(update, context):
    user_input = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )
    bot_response = response['choices'][0]['text']
    update.message.reply_text(bot_response)

def main():
    token = '6551801424:AAEvoJmcTvxbEoVx6_RdfuokyUBrd7qUFS8'
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
