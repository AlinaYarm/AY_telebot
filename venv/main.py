import telebot
import os
import random

from telebot import types

TOKEN = os.getenv('TELE_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    # start_btn = telebot.types.KeyboardButton("/start")
    help_btn = telebot.types.KeyboardButton("/help")
    markup.add(help_btn)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
item1 = types.KeyboardButton('Нажми на кнопку, и я тебе отправлю имя твоего собеседника')

markup.add(item1)

companion = ['Аня', 'Павел', 'Анастасия', 'Григорий', 'Азамат', 'Денис', 'Алия']

@bot.message_handler(content_types=['text', 'photo'])
def messagelist(message):
    if massage.text == 'Нажми на кнопку, и я тебе отправлю имя твоего собеседника':
        bot.send_message(massage.chat.id, random.choice(companion))
    else:
        bot.send_message(massage.chat.id, 'Ничего не понял')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Введите дату в формате ГГГГ-ММ-ДД')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = message.text
    bot.send_message(message.from_user.id, msg)


bot.polling(none_stop=True, interval=0)

