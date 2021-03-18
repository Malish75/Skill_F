# -*- coding: utf-8 -*-
import telebot
from config import currencys, TOKEN
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def start_help(message: telebot.types.Message):
    text = 'Бот считает, сколько нужно одной валюты для перевода в количество\
    другой.\nФормат ввода: <исходная валюта> <конечная валюта> <количество>\nНапример: \
    рубль евро 200\nДоступные валюты - /values '
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    currencys_list = [key for key in currencys.keys()]
    text = "Доступные валюты:\n" + ", ".join(currencys_list)
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        input_ = message.text.split()
        if len(input_) != 3:
            raise APIException("Неверное количество данных.")
        quote, base, amount = input_
        val = CurrencyConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f'{amount} {base}  - это {val} {quote}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)