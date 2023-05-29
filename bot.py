
import telebot


import os

os.environ["DJANGO_SETTINGS_MODULE"] = "dp.settings"

import django
django.setup()

from main.models import QnA

bot = telebot.TeleBot(
    "6000072399:AAH9bWicGVn_GnIOpTgLvwRNFiHcru6Fp3o", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "Добро пожаловать! Это бот поддержки для КГУ им. Ишеналы Арабаева. Я могу ответить на ваши вопросы!")


@bot.message_handler(func=lambda m: True)
def reply_tree(message):

    txt = message.text
    obj = QnA.objects.get(question=txt.lower())
    if obj:
        bot.send_message(message.chat.id, obj.answer)
    else:
        bot.send_message(message.chat.id, 'Не понимаю ваш запрос, извините.')

bot.infinity_polling()