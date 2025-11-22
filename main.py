import telebot

# Seu token do bot
TOKEN = '8571350639:AAFOEin6lzTPnhs_sG0LrBReOVW_Fvu8OAE'

bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou seu bot. Como posso ajudar?")

# Comando /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Comandos disponíveis:\n/start - Iniciar\n/help - Ajuda")

# Responde a qualquer mensagem de texto
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Você disse: {message.text}")

# Mantém o bot rodando
print("Bot está rodando...")
bot.infinity_polling()
