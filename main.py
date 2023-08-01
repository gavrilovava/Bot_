import telebot
from telebot import types
bot = telebot.TeleBot('6286042823:AAHldjUbE-EJAV-OkOAHXGBRtPWQTTbhMK0');
from src1.person import *
from src1.constant import bot_tex

@bot.message_handler(content_types=['text'])

def start(message):
    if message.text == '/start':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(bot_tex.first)
        btn2 = types.KeyboardButton(bot_tex.play)
        btn3 = types.KeyboardButton(bot_tex.edit)
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, bot_tex.four, reply_markup=markup)
        bot.register_next_step_handler(message, get_text_messages);


bot.polling(none_stop=True, interval=0)