import env as keys
from telegram.ext import *
import responses as r
import time
import links


print("Bot started...")


def start_command(update, context):
    update.message.reply_text("Type start something.")


def help_command(update, context):
    update.message.reply_text("If you need to help. Go to google search.")
    update.message.reply_text("Link below.")
    time.sleep(3)
    update.message.reply_text(links.google)


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
