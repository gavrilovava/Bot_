import telebot
from telebot import types

from src1.game import *
from src1.constant import person, bot
    
def get_text_messages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == bot_tex.play and person.creat:
        game(message)
    elif message.text == bot_tex.play:
        bot.send_message(message.from_user.id, bot_tex.noper, reply_markup=markup)
        bot.register_next_step_handler(message, get_text_messages);
    elif message.text == bot_tex.edit:
        bot.send_message(message.from_user.id, bot_tex.pas, reply_markup=markup)
        bot.register_next_step_handler(message, teacher);
    else: 
        person.creat = True      
        choose_pic(message)



def choose_pic(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_photo(message.from_user.id, photo=open(person.type1, 'rb'), caption='1')
    bot.send_photo(message.from_user.id, photo=open(person.type2, 'rb'), caption='2')
    bot.send_photo(message.from_user.id, photo=open(person.type3, 'rb'), caption='3')
    bot.send_photo(message.from_user.id, photo=open(person.type4, 'rb'), caption='4')
    btn1 = types.KeyboardButton(bot_tex.t1)
    btn2 = types.KeyboardButton(bot_tex.t2)
    btn3 = types.KeyboardButton(bot_tex.t3)
    btn4 = types.KeyboardButton(bot_tex.t4)
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, bot_tex.chap, reply_markup=markup)
    bot.register_next_step_handler(message, set_pic);

def set_pic(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == bot_tex.t1:
        person.style = person.type1

    elif message.text == bot_tex.t2:
        person.style = person.type2

    elif message.text == bot_tex.t3:
        person.style = person.type3

    elif message.text == bot_tex.t4:
        person.style = person.type4
    bot.send_message(message.from_user.id, bot_tex.good, reply_markup=markup)
    choose_name(message)

def choose_name(message):
    bot.send_message(message.from_user.id, bot_tex.name)
    bot.register_next_step_handler(message, set_name);

def set_name(message):
    person.name = message.text
    bot.send_message(message.from_user.id, bot_tex.ynm + person.name)
    show_person(message)  

def show_person(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(bot_tex.play)
    btn2 = types.KeyboardButton(bot_tex.first)
    markup.add(btn1, btn2)
    bot.send_photo(message.from_user.id, photo=open(person.style, 'rb'))
    choise(message)

def choise(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(bot_tex.first)
    btn2 = types.KeyboardButton(bot_tex.play)
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, bot_tex.ready, reply_markup=markup)
    bot.register_next_step_handler(message, get_text_messages);

