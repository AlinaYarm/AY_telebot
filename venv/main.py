import telebot

import os
import random

from telebot import types

TOKEN = os.getenv('TELE_TOKEN')
bot = telebot.TeleBot(TOKEN)
companion = ['Аня', 'Павел', 'Анастасия', 'Григорий', 'Азамат', 'Денис', 'Алия']

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Начать чаепитие")
    help_btn = telebot.types.KeyboardButton("/help")
    markup.add(btn1, btn2, help_btn)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот, который рандомно выберет тебе собеседника для совместного чаепития".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что ты с нами!)")
    elif (message.text == "Начать чаепитие"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tea = telebot.types.KeyboardButton("Пора пить чай!")
        markup.add(tea)
        bot.send_message(message.chat.id, 'Нажми на кнопку "Пора пить чай!", и я тебе отправлю имя твоего собеседника!',
                         reply_markup=markup)
    elif (message.text == "Пора пить чай!"):
        if message.text == 'Пора пить чай!':
            bot.send_message(message.chat.id, random.choice(companion))
        else:
            bot.send_message(message.chat.id, 'Ничего не понял')

    elif (message.text == "/help"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Выбрать тебе собеседника")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("/help")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")


#@bot.message_handler(content_types=['text', 'photo'])
#def messagelist(message):
    #if message.text == 'Пора пить чай!':
        #bot.send_message(message.chat.id, random.choice(companion))
    #else:
        #bot.send_message(message.chat.id, 'Ничего не понял')

bot.polling(none_stop=True)

