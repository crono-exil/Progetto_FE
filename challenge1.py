import telebot

#SOSTIUISCI IL TOKEN CON QUELLO DEL BOT DESIDERATO!!!
token = "7313459074:AAHLSHn03EsmUKCKguZdMbKODQHyk57NBBU"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Benvenuto!")



@bot.message_handler(commands=["reverse"])
def send_message(message):
    bot.reply_to(message,"Dammi una parola")
    @bot.message_handler(func=lambda msg: True)
    def messaggio_contrario(message):
        messaggio=reverse_string(message.text)
        bot.reply_to(message, messaggio)
        if message.text==messaggio :
            bot.send_message(message.chat.id, "Questa parola e' palindroma")
        else:
            bot.send_message(message.chat.id, "Questa parola non e' palindroma")
    def reverse_string(message):
        return message[::-1]


bot.infinity_polling()


