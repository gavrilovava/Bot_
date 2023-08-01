import telebot
from telebot import types

from src1.teacher import *
from src1.constant import game_p, zero_level, first_level, bot_tex, bot

def zero(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(bot_tex.task_1)
    btn2 = types.KeyboardButton(bot_tex.task_2)
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, bot_tex.five, reply_markup=markup)
    bot.register_next_step_handler(message, zero_l);
            
def zero_l(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == bot_tex.task_1:
        game_p.now_task = 0
    elif message.text == bot_tex.task_2:
        game_p.now_task = 1
    if (game_p.now_level == 0):
        if (zero_level.done_task[game_p.now_task]):
            bot.send_message(message.from_user.id, zero_level.text_task[game_p.now_task], reply_markup=markup)
            bot.register_next_step_handler(message, nomer_z);
        else:
            bot.send_message(message.from_user.id, bot_tex.six, reply_markup=markup)
            game(message)
    else:
        if (first_level.done_task[game_p.now_task]):
            bot.send_message(message.from_user.id, first_level.text_task[game_p.now_task], reply_markup=markup)
            bot.register_next_step_handler(message, nomer_z);
        else:
            bot.send_message(message.from_user.id, bot_tex.six, reply_markup=markup)
            game(message)        
            
def nomer_z(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if ((message.text == str(zero_level.answer[game_p.now_task])) and (game_p.now_level == 0)):
        bot.send_message(message.from_user.id, bot_tex.seven, reply_markup=markup)
        zero_level.done_task[game_p.now_task] = False
        game_p.hart_level = game_p.hart_level + game_p.hart
        game(message)
    elif ((message.text == str(first_level.answer[game_p.now_task])) and (game_p.now_level == 1)):
        bot.send_message(message.from_user.id, bot_tex.seven, reply_markup=markup)
        first_level.done_task[game_p.now_task] = False
        game_p.hart_level = game_p.hart_level + game_p.hart
        game(message)
    elif (message.text == bot_tex.swap) and game_p.switch:
        bot.send_message(message.from_user.id, bot_tex.eight, reply_markup=markup)
        game_p.switch = False
        game(message)
    else:
        bot.send_message(message.from_user.id, bot_tex.change, reply_markup=markup)
        game_p.switch = True
        bot.register_next_step_handler(message, nomer_z);


def game(message):
    for i in range((game_p.hart_level // game_p.hart)):
        if (i < 1) and not (str(i + 1) in game_p.lev):
            a = str(i + 1)
            game_p.lev = game_p.lev + ", " + a
    bot.send_message(message.from_user.id,  bot_tex.choose + game_p.lev)
    bot.register_next_step_handler(message, choose_level)
    
    

def choose_level(message):
    if message.text == bot_tex.t_0 and (bot_tex.t_0 in game_p.lev):
        game_p.now_level = 0
        zero(message)
    elif message.text == bot_tex.t_1 and (bot_tex.t_1 in game_p.lev):
        game_p.now_level = 1
        zero(message)
    else:
        bot.send_message(message.from_user.id, bot_tex.uncorch)
        game(message)
