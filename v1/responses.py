from datetime import datetime
from v1 import links


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "привіт", "hello!", "hi!", "привіт!"):
        return "Hello!"

    if user_message in ("how are you", "how's it going", "how are you?", "how's it going?", "як справи", "як справи?"):
        return "Excellent!"

    if user_message in ("who are you", "who are you?", "хто ти?"):
        return "I am Simple Bot. My username agent007_superbot." \
               "=)"

    if user_message in ("show you self", "show you self.", "покажи себе", "покажи себе."):
        return links.image_007

    if user_message in ("cool", "cool!", "круто", "круто!"):
        return links.image_cool

    if user_message in ("time", "time.", "час", "час."):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("bye", "bye!", "пака", "пака!", "бувай", "бувай!"):
        return "Bye!"

    return "I don't understand you."
