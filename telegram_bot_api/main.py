import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.API_KEY)


@bot.message_handler(commands=["start"])
def sample_message(message):
    sti = open("static/welcome.webp", 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("😋 Випадкове число")
    item2 = types.KeyboardButton("🤩 Як справи?")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Ласкаво просимо, {0.first_name}!\nЯ - "
                                      "<b>{1.first_name}</b>".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=["cool"])
def cool_message(message):
    sti = open("static/cool.tgs", 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "{0.first_name}!\nЯ - крутий!".format(message.from_user),
                     parse_mode='html')


@bot.message_handler(content_types=["text"])
def sample_message(message):
    if message.chat.type == 'private':
        if message.text == "😋 Випадкове число":
            bot.send_message(message.chat.id, str(random.randint(1, 100)))
        elif message.text == "🤩 Як справи?":
            bot.send_message(message.chat.id, "Чудово!")
        else:
            bot.send_message(message.chat.id, "Окей, тоді бувай!🖐")


def main():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
