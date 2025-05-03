import telebot

# این توکن رو از BotFather گرفتی. بعداً جایگزین کن.
TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
