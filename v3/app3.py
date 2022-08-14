import config_3
from telegram.ext import *
from telegram import Update
import time

updater = Updater(config_3.API_KEY, use_context=True)

print("Bot started")


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Welcome user! Click on in order to select hint to search /help")


def help(update: Update, context: CallbackContext):
	update.message.reply_text(
		"""Select reply column:
	/Google - To find something information.
	/Youtube - To watch something interesting video.
	/Instagram - To check activity in social media.
	/Weather forecast - To watch weather forecast today.
	/Exit.""")


def google(update: Update, context: CallbackContext):
	update.message.reply_text("Google search 🌐 🔍 \n")
	time.sleep(2)
	update.message.reply_text("Site URL => https://www.google.com/")


def youtube(update: Update, context: CallbackContext):
	update.message.reply_text("Youtube 📹 \n")
	time.sleep(2)
	update.message.reply_text("Site URL => https://www.youtube.com/")


def instagram(update: Update, context: CallbackContext):
	update.message.reply_text("Instagram 📱 \n")
	time.sleep(2)
	update.message.reply_text("Site URL => http://www.instagram.com/")


def weather(update: Update, context: CallbackContext):
	update.message.reply_text("Weather forecast 🌤 \n")
	time.sleep(2)
	update.message.reply_text("Site URL => https://ua.sinoptik.ua/")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Your text '%s' bot haven't information." % update.message.text)
	time.sleep(2)
	update.message.reply_text("Select information with \ /help.")


def exit(update: Update, context: CallbackContext):
	update.message.reply_text("Bye 👋!")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('google', google))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram))
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('exit', exit))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))


def main():
	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	main()
