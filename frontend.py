import os
import requests
from dotenv import load_dotenv
import telebot

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BACKEND_URL = "http://127.0.0.1:8000"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['help'])
def help_command(message):
    response = requests.get(f"{BACKEND_URL}/help/")
    if response.status_code == 200:
        bot.send_message(message.chat.id, response.json()["text"])
    else:
        bot.send_message(message.chat.id, "⚠️ Errore nel recuperare le informazioni di aiuto.")



# Avvio del bot
bot.polling()
