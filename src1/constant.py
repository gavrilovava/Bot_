import telebot
bot = telebot.TeleBot('6286042823:AAHldjUbE-EJAV-OkOAHXGBRtPWQTTbhMK0');

class game_p():
    level = 0
    hart_level = 0
    lev = "0"
    switch = False
    now_task = 0
    now_level = 0
    hart = 5

class zero_level():
    done_task = [True, True]
    text_task = ['условие задачи ответ 15', 'условие задачи ответ 3']
    answer = [15, 3]

class first_level():
    done_task = [True, True]
    text_task = ['условие задачи ответ 14', 'условие задачи ответ 6']
    answer = [14, 6]

class t():
    password = "12345"
    name = 100
    level = 100
    nots = False
    nott = False

class person():
    name = ''
    namep = False
    style = "photo/ups.jpg"
    creat = False
    type1 = "photo/girl1.png"
    type2 = "photo/girl2.png"
    type3 = "photo/boy1.png"
    type4 = "photo/boy2.png"

class bot_tex():
    first = 'Создать/редактировать персонажа'
    play = 'Играть'
    four = "Создай своего персонажа и начни играть"
    task_1 = '№1'
    task_2 = '№2'
    five = "Выбери задачу"
    six = "Ты уже решал эту задачу"
    seven = "УРА ПРАВИЛЬНО"
    swap = 'другая'
    eight = "Не грусти, решишь в другой раз"
    change = "Попробуй еще раз или напиши слово другая"
    choose = "Выберите уровень: "
    uncorch = "Неправильно выбран уровень"
    noper = "Персонаж не создан"
    edit = 'Режим редактора'
    pas = "Введите пароль"
    chap = "Выбери как будет выглядеть персонаж"
    good = "Отлично"
    name = "Напиши имя твоего персонажа"
    t1 = '$1'
    t2 = '$2'
    t3 = '$3'
    t4 = '$4'
    t_0 = '0'
    t_1 = "1"
    ynm = "Твоего персонажа зовут "
    ready = "Наш персонаж готов, можем начинать играть."

class bot_text_edit():
    come_ed = "Вы вошли в режим редактора"
    wrong = "Неверный пароль, перезапустите бота кнопкой /start"
    zero = 'нулевой'
    first = 'первый'
    choose = "Выберите уровень для редактирование"
    choose_task = "Выберите задачу для редактирование"
    task1 = 'задача 1'
    task2 = 'задача 2'
    new_task = "Введите новый текст задачи"
    new_answer = "Введите новый ответ на задачу"