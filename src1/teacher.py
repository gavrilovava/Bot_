import telebot
from telebot import types

from src1.constant import t, first_level, zero_level, bot_text_edit, bot

def teacher(message):
    if message.text == t.password:
        bot.send_message(message.from_user.id, bot_text_edit.come_ed)
        ch(message)
    else:
        bot.send_message(message.from_user.id, bot_text_edit.wrong)

def ch(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(bot_text_edit.zero)
    btn2 = types.KeyboardButton(bot_text_edit.first)
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, bot_text_edit.choose, reply_markup=markup)
    bot.register_next_step_handler(message, diff);

def diff(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == bot_text_edit.zero:
        t.level = 0
        t.nots = True
    elif message.text == bot_text_edit.first:
        t.level = 1
        t.nots = True
    if t.nots: 
        t.nots = False   
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(bot_text_edit.task1)
        btn2 = types.KeyboardButton(bot_text_edit.task2)
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, bot_text_edit.choose_task, reply_markup=markup)
        bot.register_next_step_handler(message, diff_0)

def diff_0(message):
    if message.text == bot_text_edit.task1:
        t.name = 0
        t.nott = True
    elif message.text == bot_text_edit.task2:
        t.name = 1
        t.nott
    if t.nott:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, bot_text_edit.new_task, reply_markup=markup)
        bot.register_next_step_handler(message, set_text_0);

def set_text_0(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if t.level == 0:
        zero_level.text_task[t.name] = message.text
    elif t.level == 1:
        first_level.text_task[t.name] = message.text
    bot.send_message(message.from_user.id, bot_text_edit.new_answer, reply_markup=markup)
    bot.register_next_step_handler(message, set_answer_0);

def set_answer_0(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if t.level == 0:
        zero_level.answer[t.name] = message.text
    elif t.level == 1:
        first_level.answer[t.name] = message.text
    ch(message)
