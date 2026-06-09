#ATTENZIONE AGGIUSTARE IL PERCOROSO DEI FILE NELLE RIGHE COMMENTATE

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

#SOSTIUISCI IL TOKEN CON QUELLO DEL BOT DESIDERATO!!!
token = "7313459074:AAHLSHn03EsmUKCKguZdMbKODQHyk57NBBU"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Benvenuto! Usa /buttons per vedere le opzioni.")

@bot.message_handler(commands=["buttons"])
def button_handler(message):
    markup = ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    markup.add(
        KeyboardButton("Immagine"),
        KeyboardButton("Testo"),
        KeyboardButton("Audio")
    )
    send_msg = bot.send_message(message.chat.id, "Cosa preferisci?", reply_markup=markup)
    bot.register_next_step_handler(send_msg, buttons_next_step)

def buttons_next_step(message):
    if message.text == "Immagine":
        with open("duck.jpg", "rb") as img:    #AGGIUSTARE DIRECTORY
            bot.send_photo(message.chat.id, img)
    elif message.text == "Testo":
        bot.send_message(message.chat.id, "Ecco il testo che hai richiesto!")
    elif message.text == "Audio":
        with open("suono.mp3", "rb") as audio:  #AGGIUSTARE DIRECTORY
            bot.send_audio(message.chat.id, audio)
    else:
        bot.send_message(message.chat.id, "Scelta non valida. Usa /buttons per riprovare.")


bot.infinity_polling()
