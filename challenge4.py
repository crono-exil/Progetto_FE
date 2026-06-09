#ATTENZIONE AGGIUSTARE IL PERCOROSO DEI FILE NELLE RIGHE COMMENTATE

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


#SOSTIUISCI IL TOKEN CON QUELLO DEL BOT DESIDERATO!!!
token = "7313459074:AAHLSHn03EsmUKCKguZdMbKODQHyk57NBBU"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Benvenuto! Usa /buttons per vedere le opzioni.")

@bot.message_handler(commands=["buttons"])
def button_handler(message):
    markup = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    markup.add(
        KeyboardButton("Inline_Buttons")
    )
    send_msg = bot.send_message(message.chat.id, "Premi il bottone per evitare errori di scrittura.", reply_markup=markup)
    bot.register_next_step_handler(send_msg, buttons_next_step)

def buttons_next_step(message):
    if message.text == "Inline_Buttons":

        markup1 = InlineKeyboardMarkup(row_width=3)
        markup1.add(
            InlineKeyboardButton("Immagine", callback_data="image"),
            InlineKeyboardButton("Testo", callback_data="text"),
            InlineKeyboardButton("Audio", callback_data="audio"),
        )
        bot.send_message(message.chat.id, "Scegli il tipo di messaggio da ricevere.", reply_markup=markup1)
        
        @bot.callback_query_handler(func=lambda call: True)
        def option_handler(call):
            if call.data == "image":
                with open("duck.jpg", "rb") as img:    #AGGIUSTARE DIRECTORY
                    bot.send_photo(message.chat.id, img)
            elif call.data == "text":
                bot.send_message(message.chat.id, "Ecco il testo che hai richiesto!")
            elif call.data == "audio":
                with open("suono.mp3", "rb") as audio:  #AGGIUSTARE DIRECTORY
                    bot.send_audio(message.chat.id, audio)




bot.infinity_polling()


